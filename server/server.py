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
import math
from motion import boot_motion

RUN_CAM = False
ENTROPY_SAMPLE = []


app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)


def get_temp_path(name):
    tempdir = tempfile.mkdtemp()
    date = datetime.now()
    filename = '{}-{}.jpg'.format(name, date)
    path = os.path.join(tempdir, filename)
    return path

def open_image(path):
    img_str = ''
    with open(path, "rb") as imageFile:
        img_str = 'data:image/jpeg;base64,' + base64.b64encode(imageFile.read())
    return img_str
        

def snap():
    img_str = ''
    camera = picamera.PiCamera()
    
    try:
        path = get_temp_path('capture')
        camera.capture(path)
        img_str = open_image(path)
    except (ValueError, RuntimeError, TypeError, NameError):
        logging.exception("could not capture image")
    finally:
        camera.close()
    return  (img_str, path)

@app.route('/take')
def take_picture():
    img_str, _ = snap()
    response = Response(
        response = json.dumps({
            'src': img_str
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
    def send_motion_event():
        emit('motion-detected', {'motion': 'found some motion'})

    @copy_current_request_contest
    def motion_exit():
        emit('motion-detector-exit', {'exit': 'exited'})
        
                
    if message == 'on':
        RUN_CAM = True
        response = "on"
    else:
        RUN_CAM = False
        response = "off"
    boot_motion(send_motion_event, motion_exit)
    emit('motion response', {'data': response})

@socketio.on('disconnect')
def stop_detector():
    global RUN_CAM
    RUN_CAM = False
        

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=80)
