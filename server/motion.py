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
    def __init__(self, cb, resolution=(CAMERA_WIDTH, CAMERA_HEIGHT), framerate=CAMERA_FRAMERATE, rotation=0, hflip=False, vflip=False):
        self.camera = None
        self.cb = cb

    def capture_image(self):
        stream = BytesIO()
        self.camera.capture(stream, format='jpeg')
        stream.seek(0)
        im = Image.open(stream)
        im_buffer = im.load()
        return im, im_buffer

    def pix_diff(self, x,y, im_buff_1, im_buff_2):
        pix_abs = abs(im_buff_1[x,y][1] - im_buff_2[x,y][1])
        if pix_abs > THRESHOLD:
            return True
        else:
            return False
        
    def check_for_motion(self, im_buffer_1, im_buffer_2):
        motion_detected = False
        changed_list = [self.pix_diff(x,y,im_buffer_1, im_buffer_2) for x,y in zip(xrange(0, CAMERA_WIDTH), xrange(0,CAMERA_HEIGHT))]
        changed_pixels = sum(changed_list)
        if changed_pixels > SENSITIVITY:
            return True, changed_pixels
        else:
            return False, changed_pixels
        
    def detector(self):
        im_1, im_1_buffer = self.capture_image()
        while True:
            if not RUN_CAM:
                self.stop()
                break
            im_2, im_2_buffer = self.capture_image()
            motionDetected, pixChanges = self.check_for_motion(im_1_buffer, im_2_buffer)
            self.cb(pixChanges, motionDetected)
            im_1, im_1_buffer = im_2, im_2_buffer

    

    def stop(self):
        # set thread indicator to stop thread
        self.camera.close()
        self.camera = None

    def start(self):
        self.camera = PiCamera()
        self.camera.resolution=(CAMERA_WIDTH, CAMERA_HEIGHT)
        time.sleep(2.0)
        t = Thread(target=self.detector)
        t.daemon = True
        t.start()
    
def boot_motion(cb, exit_func):
    try:
        md = MotionDetector(cb)
        md.start()
    except:
        e = sys.exc_info()[0]
        exit_func(e)

def stop_cam():
    global RUN_CAM
    RUN_CAM = False
    return

def start_cam():
    global RUN_CAM
    RUN_CAM = True
    return

def restart_motion():
    if RUN_CAM:
        stop_cam()
        time.sleep(2)
        start_cam()

def set_sensitivity(sensitivity):
    global SENSITIVITY
    SENSITIVITY = sensitivity
    restart_motion()

def set_threshold(threshold):
    global THRESHOLD
    THRESHOLD = threshold
    restart_motion()

def get_threshold():
    return THRESHOLD

def get_sensitivity():
    return SENSITIVITY
