from PIL import Image
import time
import datetime
from io import BytesIO
from picamera import PiCamera
from threading import Thread
import math

THRESHOLD = 10
SENSITIVITY = 20

CAMERA_WIDTH = 100
CAMERA_HEIGHT = 100
CAMERA_HFLIP = True
CAMERA_VFLIP = True
CAMERA_ROTATION = 0
CAMERA_FRAMERATE = 35

RUN_CAM = True

class MotionDetector:
    def __init__(self, resolution=(CAMERA_WIDTH, CAMERA_HEIGHT), framerate=CAMERA_FRAMERATE, rotation=0, hflip=False, vflip=False):
        self.camera = PiCamera()
        self.camera.resolution=(CAMERA_WIDTH, CAMERA_HEIGHT)
        self.current_frame=None
        self.stopped = False

    def start(self):
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        self.current_frame = self.capture_image
        

    def capture_image(self):
        stream = BytesIO()
        self.camera.capture(stream, format='jpeg')
        stream.seek(0)
        im = Image.open(stream)
        im_buffer = im.load()
        return im, im_buffer

    def stop(self):
        # set thread indicator to stop thread
        self.stopped = True

def pix_diff(x,y, im_buff_1, im_buff_2):
    pix_abs = abs(im_buff_1[x,y][1] - im_buff_2[x,y][1])
    if pix_abs > THRESHOLD:
        return True
    else:
        return False
    
def checkForMotion(im_buffer_1, im_buffer_2):
    motion_detected = False
    changed_list = [pix_diff(x,y,im_buffer_1, im_buffer_2) for x,y in zip(xrange(0, CAMERA_WIDTH), xrange(0,CAMERA_HEIGHT))]
    changed_pixels = sum(changed_list)
    if changed_pixels > SENSITIVITY:
        return True, changed_pixels, SENSITIVITY
    else:
        return False, changed_pixels, SENSITIVITY

def main(md, cb):
    im_1, im_1_buffer = md.capture_image()
    while RUN_CAM:
        im_2, im_2_buffer = md.capture_image()
        motionDetected, pixChanges, sensitivity = checkForMotion(im_1_buffer, im_2_buffer)
        if motionDetected:
            print("GOT MOTION", pixChanges)
            cb(pixChanges,sensitivity)
        else:
            print("NOTHING", pixChanges)
        im_1, im_1_buffer = im_2, im_2_buffer
        
def boot_motion(cb, exit_func):
    try:
        md = MotionDetector()
        time.sleep(2.0)
        main(md, cb)
    finally:
        exit_func()

def stop_cam():
    global RUN_CAM
    RUN_CAM = False

def start_cam():
    global RUN_CAM
    RUN_CAM = True
