from flask import Flask, Response, send_file, json, request, copy_current_request_context
from io import BytesIO
import base64
import time
from PIL import Image, ImageChops
import tempfile
import logging
from datetime import datetime
import os
import picamera
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit
import threading
import numpy as np

RUN_CAM = False


app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)


def image_entropy(img):
    w,h = img.size
    a = np.array(img.convert('RGB')).reshape((w*h,3))
    h,e = np.histogramdd(a, bins=(16,)*3, range=((0,256),)*3)
    prob = h/np.sum(h) # normalize
    prob = prob[prob>0] # remove zeros
    return -np.sum(prob*np.log2(prob))

def analyze_images(img_path_1, img_path_2):
    img1 = Image.open(img_path_1)
    img2 = Image.open(img_path_2)
    path = get_temp_path('diff')
    img_diff = ImageChops.difference(img1, img2)
    img_diff.save(path)
    entropy = image_entropy(img_diff)
    logging.debug(entropy)

def get_temp_path(name):
    tempdir = tempfile.mkdtemp()
    date = datetime.now()
    filename = '{}-{}.jpg'.format(name, date)
    path = os.path.join(tempdir, filename)
    return path
        

def snap():
    img_str = ''
    camera = picamera.PiCamera()
    
    try:
        path = get_temp_path('capture')
        camera.capture(path)
        with open(path, "rb") as imageFile:
            img_str = base64.b64encode(imageFile.read())
    except (ValueError, RuntimeError, TypeError, NameError):
        logging.exception("could not capture image")
    finally:
        camera.close()
    current_img_str = 'data:image/jpeg;base64,' + img_str
    return  (current_img_str, path)

@app.route('/take')
def take_picture():
    img_str = snap()
    response = Response(
        response = json.dumps({
            'src': 'data:image/jpeg;base64,' + img_str
        }),
        status = 200,
        mimetype='application/json'
    )
    return response

@socketio.on('motion')
def check_motion(message):
    logging.debug(message)
    global RUN_CAM
    response = None
    @copy_current_request_context
    def run_motion_cam(emit_func):
        img_1, img_1_path = None
        while RUN_CAM:
            img_2_str, img_2_path = None
            if not img_1 or img_1_path:
                img_1_str, img_1_path = snap()
                emit_func( "detector running", {'pic': img_1_str})
                time.sleep(1)
                img_2_str, img_2_path = snap()
                emit_func( "detector running", {'pic': img_2_str})
            else:
                img_2_str, img_2_path = snap()
                emit_func( "detector running", {'pic': img_2_str})
                img_1_str = img_2_str
                img_1_path = img_2_path
            time.sleep(5)
        
    def run_detector(run_cam, emit_func):
        logging.debug(run_cam)
        cam_thread = None

        if run_cam:
            cam_thread = threading.Thread(target=run_motion_cam, args=[emit_func])
            cam_thread.start()
        else:
            if cam_thread:
                logging.debug('stopping thread')
                cam_thread.stop()
                
    if message == 'on':
        RUN_CAM = True
        response = "on"
    else:
        RUN_CAM = False
        response = "off"
    logging.debug(response)
    emit('motion response', {'data': response})
    run_detector(RUN_CAM, emit)

@socketio.on('disconnect')
def stop_detector():
    global RUN_CAM
    RUN_CAM = False
        

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=80)
