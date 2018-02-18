from flask import Flask, Response, send_file, json
from io import BytesIO
import base64
import time
from PIL import Image
import tempfile
import logging
from datetime import datetime
import os
import picamera


app = Flask(__name__)

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
    finally:
        print("captured image")
    response = Response(
        response = json.dumps({
            'data': 'data:image/jpeg;base64,' + img_str
        }),
        status = 200,
        mimetype='application/json'
    )
    camera.close()
    return response

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
