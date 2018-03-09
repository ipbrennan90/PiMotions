from PIL import Image
from io import BytesIO
from picamera import PiCamera
import time
import tempfile
import os
from datetime import datetime
import logging
import base64


CAMERA_WIDTH = 100
CAMERA_HEIGHT = 100
CAMERA_HFLIP = True
CAMERA_VFLIP = True
CAMERA_ROTATION = 0
CAMERA_FRAMERATE = 35

def get_temp_path(name):
    tempdir = tempfile.mkdtemp()
    date = datetime.now()
    filename = '{}-{}.jpg'.format(name, date)
    path = os.path.join(tempdir, filename)
    return path

def get_base_64_img_str(path):
    img_str = ''
    with open(path, "rb") as imageFile:
        img_str = 'data:image/jpeg;base64,' + base64.b64encode(imageFile.read())
    return img_str

class Camera:
    def __init__(self, width=CAMERA_WIDTH, height=CAMERA_HEIGHT, framerate=CAMERA_FRAMERATE, rotation=0, hflip=False, vflip=False):
        self.device = None
        self.resolution = (width, height)
        self.rotation = rotation
        self.framerate = framerate
        self.hflip = hflip
        self.vflip = vflip
        self.width = width
        self.height = height

    def start(self):
        self.device = PiCamera()
        self.device.resolution = self.resolution
        self.device.rotation = self.rotation
        self.device.framerate = self.framerate
        self.device.hflip = self.hflip
        self.device.vflip = self.vflip
        time.sleep(2.0)

    def stop(self):
        self.device.close()
        self.device = None
    
    def capture_image(self):
        stream = BytesIO()
        self.device.capture(stream, format='jpeg')
        stream.seek(0)
        im = Image.open(stream)
        im_buffer = im.load()
        return im_buffer
    
    def capture_b64_image(self):
        img_str = ''
        self.start()
        try:
            path = get_temp_path('capture')
            self.device.capture(path)
            img_str = get_base_64_img_str(path)
        except (ValueError, RuntimeError, TypeError, NameError):
            logging.exception("could not capture image")
        finally:
            self.stop()
        return  (img_str, path)

    


