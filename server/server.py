from flask import Flask, Response, render_template, send_file, json
from io import BytesIO
import base64
import time
from PIL import Image
import tempfile
import logging
from datetime import datetime
import os
try:
    import local_config
except ImportError:
    # we want to fail silently here since all this means is that
    # we are running on pi, not locally
   pass

if "PI" not in os.environ:
    import picamera


app = Flask(__name__, static_folder="../static/dist", template_folder="../static")


def check_pi():
    if "PI" in os.environ and os.environ["PI"] == "none":
        return False
    else:
        return True
    
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/take')
def take_picture():
    is_pi = check_pi()
    if is_pi == False:
        response = Response(
            response = json.dumps({
                'data': 'no image'
            }),
            status = 200,
            mimetype='application/json'
        )
        return response
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
