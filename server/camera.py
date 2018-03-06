from PIL import Image
from io import BytesIO
from picamera import PiCamera

CAMERA_WIDTH = 100
CAMERA_HEIGHT = 100
CAMERA_HFLIP = True
CAMERA_VFLIP = True
CAMERA_ROTATION = 0
CAMERA_FRAMERATE = 35

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
        self.camera.capture(stream, format='jpeg')
        stream.seek(0)
        im = Image.open(stream)
        im_buffer = im.load()
        return im_buffer

    

    

