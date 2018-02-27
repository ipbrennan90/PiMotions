import time
import datetime
from picamera import PiCamera
from picamera.array import PiRGBArray
from threading import Thread
import math

THRESHOLD = 20
SENSITIVITY = 300

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

def abs_array(array1, array2):
   return [abs(v1-v2) > THRESHOLD for v1, v2 in zip(array1, array2)]

def abs_matrix(matrix1, matrix2):
    matrix_abs_matrix = [abs_array(array1, array2) for array1, array2 in zip(matrix1, matrix2)]
    return sum([sum(l) for l in matrix_abs_matrix])

def abs_rows(data1, data2):
    return sum([abs_matrix(matrix1, matrix2) for matrix1, matrix2 in zip(data1, data2)])

def color_matrix(matrix, i):
    return [a[i] for a in matrix]

def rgb_row_to_color_row(data, color_index):
    return [color_matrix(matrix, color_index) for matrix in data]
    
            
    
def checkForMotion(data1, data2):
    # this is where we look for motion between two data streams (RGB Arrays)
    motionDetected = False
    pixColor = 3 # this is where we select the band we are interested in (red=0, green=1, blue=2, all=3) defaults to 1
    if pixColor == 3:
        pixChanges = abs_rows(data1, data2)/3
    else:
        pixChanges = abs_matrix(rgb_row_to_color_row(data1, pixColor), rgb_row_to_color_row(data2,pixColor))

    if pixChanges > SENSITIVITY:
        motionDetected = True
    return motionDetected

def main(vs, cb):
    frame_1 = vs.read()
    while True:
        frame_2 = vs.read()
        if checkForMotion(frame_1, frame_2):
            cb()
            
        
def boot_motion(cb, exit_func):
    try:
        vs = MotionDetector().start()
        time.sleep(2.0)
        main(vs, cb)
    finally:
        exit_func()
