from threading import Thread
import time
from camera import Camera
import math
import sys

# Threshold is the threshold of change in the color value of a pixel
THRESHOLD = 10

# Sensitivity is the required number of pixels that are "changed" for motion to be detected
SENSITIVITY = 20

# A boolean to control when we run and stop the motion detector loop
RUN_DETECTOR = True

class MotionDetector:

    def __init__(self, cb):
        self.cb = cb
        self.camera = Camera()
                 
    def start(self):
        self.camera.start()
        t = Thread(target=self.detector)
        t.daemon = True
        t.start()
        
    def stop(self):
        self.camera.stop()

    def pix_diff(self, x,y, im_buff_1, im_buff_2):
        pass
        
    def check_for_motion(self, im_buffer_1, im_buffer_2):
        pass
        
    def detector(self):
        pass

    

def boot_motion(cb, exit_func):
    try:
        md = MotionDetector(cb)
        md.start()
    except:
        e = sys.exc_info()[0]
        exit_func(e)

def stop_detector():
    global RUN_DETECTOR
    RUN_DETECTOR = False
    return

def start_detector():
    global RUN_DETECTOR
    RUN_DETECTOR = True
    return

def restart_motion():
    if RUN_DETECTOR:
        stop_detector()
        time.sleep(2)
        start_detector()

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
