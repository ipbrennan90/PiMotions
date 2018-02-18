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
from flask_sockets import Sockets


app = Flask(__name__)
CORS(app)
Sockets(app)

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

@sockets.route('/motion')
def check_motion(ws):
    if request.args.get('state') == 'on':
        while not ws.closed:
            message = ws.receive
            ws.send(message)
        

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 80), app, handler_class=WebSocketHandler)
    server.serve_forever()
