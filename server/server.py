from flask import Flask, Response, send_file, json, request
from io import BytesIO
import base64
import time
from PIL import Image
import tempfile
import logging
from datetime import datetime
import os
import picamera
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit


app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

@app.route('/take')
def take_picture():
    img_str = ''
    camera = picamera.PiCamera()
    
    try:
        tempdir = tempfile.mkdtemp()
        date = datetime.now()
        filename = 'capture-{}.jpg'.format(date)
        path = os.path.join(tempdir, filename)
        camera.capture(path)
        with open(path, "rb") as imageFile:
            img_str = base64.b64encode(imageFile.read())
    except (ValueError, RuntimeError, TypeError, NameError):
        logging.exception("could not capture image")
    response = Response(
        response = json.dumps({
            'src': 'data:image/jpeg;base64,' + img_str
        }),
        status = 200,
        mimetype='application/json'
    )
    camera.close()
    return response

@socketio.on('motion on')
def check_motion(message):
    emit('motion response', {'data': 'looking for motion!'})
        

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=80)
