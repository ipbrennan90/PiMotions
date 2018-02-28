import time
import datetime
from picamera import PiCamera
from picamera.array import PiRGBArray
from threading import Thread
import math
import numpy as np

THRESHOLD = 200
SENSITIVITY = 7000

CAMERA_WIDTH = 128
CAMERA_HEIGHT = 80
CAMERA_HFLIP = True
CAMERA_VFLIP = True
CAMERA_ROTATION = 0
CAMERA_FRAMERATE = 35


class MotionDetector:
    def __init__(self, resolution=(CAMERA_WIDTH, CAMERA_HEIGHT), framerate=CAMERA_FRAMERATE, rotation=0, hflip=False, vflip=False):
        self.camera = PiCamera()
        self.camera.resolution = resolution
        self.camera.rotation = rotation
        self.camera.framerate = framerate
        self.camera.hflip = hflip
        self.camera.vflip = vflip
        self.rawCapture = PiRGBArray(self.camera, size=resolution)
        self.stream = self.camera.capture_continuous(self.rawCapture, format="rgb", use_video_port=True)
        self.stopped = False

    def start(self):
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        for f in self.stream:
            # grab frame from stream and clear stream to prep for next frame
            self.frame = f.array
            # clearing the rawCapture RGB array
            self.rawCapture.truncate(0)

            # if thread state is set stop the thread and stop camera resources
            if self.stopped:
                self.stream.close()
                self.rawCapture.close()
                self.camera.close()
                return

    def read(self):
        # return most recently read frame
        return self.frame

    def stop(self):
        # set thread indicator to stop thread
        self.stopped = True
             
def checkForMotion(data1, data2):
    motionDetected = False
    pixColor = 3 # red=0 green=1 blue=2 all=3  default=1
    if pixColor == 3:
        pixChanges = (np.absolute(data1-data2)>THRESHOLD).sum()/3
    else:
        pixChanges = (np.absolute(data1[...,pixColor]-data2[...,pixColor])>THRESHOLD).sum()
    if pixChanges > SENSITIVITY:
        motionDetected = True        
    return motionDetected, pixChanges, SENSITIVITY  

def main(vs, cb):
    frame_1 = vs.read()
    while True:
        frame_2 = vs.read()
        motionDetected, pixChanges, sensitivity = checkForMotion(frame_1, frame_2)
        if motionDetected:
            cb(pixChanges,sensitivity) 
        
def boot_motion(cb, exit_func):
    try:
        vs = MotionDetector().start()
        time.sleep(2.0)
        main(vs, cb)
    finally:
        exit_func()
