from flask import Flask, Response, render_template, send_file, json
import picamera
from io import BytesIO
import base64
import time
from PIL import Image
import tempfile
import logging
from datetime import datetime
import os



app = Flask(__name__, static_folder="../static/dist", template_folder="../static")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/take')
def take_picture():
    img_str = ''
    
    try:
        camera = picamera.PiCamera()
        time.sleep(2)
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
