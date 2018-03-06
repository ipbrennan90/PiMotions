from threading import Thread
import time
from camera import Camera
import math

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
        '''
        each pixel we grab will be an array with the RGB values of the pixel
        represented like [R, G, B] so R is the 0th index, G is the 1st index, 
        and B is the 2nd. The green band is the most sensitive to change. 
        We can access the green value of each pixel at array index 1
        '''
        green_pixel = 1
        '''
        grab the green value from our pixel from the 
        two image buffers we are comparing.
        '''
        green_val_1 = im_buff_1[x,y][1]
        green_val_2 = im_buff_2[x,y][1]
        # get the total change between the green value of the two buffers
        pix_abs = abs(green_val_1 - green_val_2)
        # check if it is greater than our threshold
        if pix_abs > THRESHOLD:
            return True
        else:
            return False
        
    def check_for_motion(self, im_buffer_1, im_buffer_2):
        motion_detected = False
        changed_pixels = []
        '''
        here we are breaking down are image buffer by column and sending the x and y 
        coordinates for each pixel to our pixel diffing function which will tell us
        how much each pixel has changed between our two images
        '''
        for x in xrange(0, self.camera.width):
            # going over each y value in our column
            for y in range(0, self.camera.height):
                # checking if the pixel has changed with our pixel diffing function
                pixel_changed = self.pix_diff(x,y,im_buffer_1, im_buffer_2)
                # adding a True or False value that was returned from pix_diff
                changed_pixels.append(pixel_changed)
        # this gives us a sum of the true values in our changed_pixels array
        total_changed_pixels = sum(changed_pixels)
        # check if the number of changed pixels is greater than our sensitivity
        if total_changed_pixels > SENSITIVITY:
            return True, total_changed_pixels
        else:
            return False, total_changed_pixels
        
    def detector(self):
        # capture our first image
        im_1_buffer = self.camera.capture_image()
        # this starts a while loop
        while True:
            # here we are checking if we still want to be running the detector
            if not RUN_DETECTOR:
                '''
                if we don't want to be running the detector we stop and break out of the loop
                this also exits the thread we started
                '''
                self.stop()
                break
            # if the loop is running we capture our second image
            im_2_buffer = self.camera.capture_image()
            # check for motion
            motionDetected, pixChanges = self.check_for_motion(im_1_buffer, im_2_buffer)
            # send the results to our callback
            self.cb(pixChanges, motionDetected)
            # set our last image as the next to be checked against for motion
            im_1_buffer = im_2_buffer

    

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
