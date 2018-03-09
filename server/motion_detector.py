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

    def pix_diff(self, pixel_one, pixel_two):
        green_val_one = pixel_one[1]
        green_val_two = pixel_two[1]

        green_change = abs(green_val_one - green_val_two)

        if green_change > THRESHOLD:
            return True
        else:
            return False
        
    def check_for_motion(self, image_one, image_two):
        motion_detected = False
        changed_pixels = []

        for x in range(0, self.camera.width):
            for y in range(0, self.camera.height):
                pixel_one = image_one[x,y]
                pixel_two = image_two[x,y]
                # we want to check the change between each pixel, that's what we use our pix diff function for
                pixel_changed = self.pix_diff(pixel_one, pixel_two)
                # this is going to be true if we see a change large enough in the pixel color
                changed_pixels.append(pixel_changed)

        total_changed_pixels = sum(changed_pixels)
        if total_changed_pixels > SENSITIVITY:
            return total_changed_pixels, True 
        else:
            return total_changed_pixels, False
        
    def detector(self):
        image_one = self.camera.capture_image()
        while RUN_DETECTOR:
            image_two = self.camera.capture_image()
            pixels_changed, motion_detected = self.check_for_motion(image_one, image_two)
            image_one = image_two
            self.cb(pixels_changed, motion_detected)
        self.stop()
    

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

def set_sensitivity(sensitivity):
    global SENSITIVITY
    SENSITIVITY = int(sensitivity)

def set_threshold(threshold):
    global THRESHOLD
    THRESHOLD = int(threshold)

def get_threshold():
    return THRESHOLD

def get_sensitivity():
    return SENSITIVITY
