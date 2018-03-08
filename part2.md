| Table Of Contents                   |
| ------------------------------------|
| [Introduction](README.md)           |
| [Part 0: Prework](prework.md)       |
| [Part 1: Pi and Web App](part1.md)  |
| Part 2: Motion Detection            |

# Part 2: Motion Detection
## Introduction

In Part 2 of this tutorial, you are going to write code to detect motion using the camera connected to your Pi.
By the end of Part 2, you will have an application that will display whether or not motion was detected in front of the camera.

## Part 2 Steps
- Write some code
- Resin sync
- Rinse, repeat

We'll mainly be working in the `server` directory, meaning that the code we write in Part 2 will be code that will run on our Pi, not on our front end. The front end code has been written for you, so once you get the Pi code working correctly, you'll have a fully functioning motion-detecting camera application, complete with front end controls for sensitivity!

### 1. Let's dive into the code!

We've set up a few small placeholder methods on this branch to get your started, but the code is not complete.

**In this section, we'll take a quick tour through some of the code that has been written for you.**

### camera.py

Open `camera.py` in your text editor. Inside the file, you'll see a camera class written for you. We're not going to modify this, but we'll make use of it in our motion-detecting code.

Our camera class has `start`, `stop`, and `capture_image` functions.

Let's look quickly at `capture_image`, since that's the one that's going to be most important for our motion-detection functionality. We've copied it below:

**Code Example 1:**
_from PiMotions/server/camera.py_:
```python {.line-numbers}
 def capture_image(self):
    stream = BytesIO()
    self.device.capture(stream, format='jpeg')
    stream.seek(0)
    im = Image.open(stream)
    im_buffer = im.load()
    return im_buffer
```

`self` is the instance of the camera class.
`self.device` is set to an instance of PiCamera in the `start` method.
```python
    self.device = PiCamera()
```
 `picamera` is a library we're imported to give us a python interface to the Raspberry Pi camera module. By setting `self.device = PiCamera()` we now have full-fledged camera functionality on instances of our Camera class. That allows us to call `self.device.capture` to take images.

The other library we need to highlight is PIL, or [Python Imaging Library](http://effbot.org/imagingbook/pil-index.htm), which we need for image processing.

Now that we've introduced the libraries, we can walk through `capture_image`.
At the beginning of the function, we read an image to a BytesIO stream (lines 2 and 3). We move to the start of the stream (line 4), and then load a PIL Image object from the stream in line 5. We then call `load` on the PIL Image object, which reads the image data and returns a pixel access object that we can use to read pixels.

If we wanted to, we could access a specific pixel in the `im_buffer` by providing the pixel coordinates (ex `im_buffer[x,y]`), which will return a tuple (a collection) of RGB values.

```python
  x = 10
  y = 12
  print(image_buffer[x,y])
```
could return something like ```(10,148,218)```, representing the R, G, and B values respectively of the pixel at that `x,y` location.

In case you were wondering, the color rgb(10, 232, 218) looks like <span style="color:#0ae8da;">this!</span>

With an understanding of our camera under our belts, let's take a quick tour through our server.py file.

### server.py

Open `server.py` in your text editor.

We're using sockets in this application, meaning that we're using real-time event-based communication between our Pi and our web app. If you don't know what that means, don't worry!

At a high level, you can think about sockets like a line of communication that stays open between the web app and the Pi. The web app and the Pi are listening on this line of communication for different events.

We can see an example of this communication by examining the code  excerpted below from `server.py`.

When the web app emits the 'motion-start' event (line 1), the Pi will take certain actions, like calling the function `start_detector()` and `boot_motion()` (lines 10 and 11 in the example below).

When the function `send_motion_event` (line 4) is called, the Pi emits a message of its own back to the web app (line 5), sending a ```"motion-detected"``` message with some data for the web app to display.

**Code Example 2:**
_from PiMotions/server/server.py_:
```python {.line-numbers}
@socketio.on('motion-start')
def check_motion():
    @copy_current_request_context
    def send_motion_event(pixChanged, motion_detected):
        emit('motion-detected', {'pixChanged': pixChanged, 'motion': motion_detected})

    @copy_current_request_context
    def motion_exit(e):
        # body of function omitted for clarity
    start_detector()
    boot_motion(send_motion_event, motion_exit)
```

Now that we know what our camera looks like and how the real-time communication works between the Pi and the web app, let's write some motion-detecting code of our own!

### 2. Motion-detection magic

All of our code is going to be written in motion-detector.py. When we get the code we need written in this file, our front end will magically work!

Open motion-detector.py in your text editor.

**A few things to notice before we start writing code:**
1) We have values for threshold, sensitivity, and whether or not our motion detector is running at the top of the file.

_from PiMotions/server/motion-detector.py_:
```python {.line-numbers}
# Threshold is the threshold of change in the color value of a pixel
THRESHOLD = 10

# Sensitivity is the required number of pixels that are "changed" for motion to be detected
SENSITIVITY = 20

# A boolean to control when we run and stop the motion detector loop
RUN_DETECTOR = True
```

2) Remember ```boot_motion(send_motion_event, motion_exit)``` from line 11, **Code Example 2**? ```boot_motion``` is the function we call when our Pi gets a message from the web app to 'motion-start'.

In `boot_motion`, we take the "send_motion_event" as one of the arguments (**Code Example 2**, line 4, and also copied below).

**Code Example 3:**
_from PiMotions/server/server.py_:
```python {.line-numbers}
@socketio.on('motion-start')
def check_motion():
    # ...
    def send_motion_event(pixChanged, motion_detected):
        emit('motion-detected', {'pixChanged': pixChanged, 'motion': motion_detected})
    # ...
    boot_motion(send_motion_event, motion_exit)
```


In motion_detector.py (excerpted below in **Code Example 4**), we can see that the first argument to `boot_motion` is a callback (cb). We use that callback in the initialization of our `MotionDetector` class (line 8). At some point (not yet implemented), we'll call that callback, which will then cause the Pi to emit the 'motion-detected' message to the web app with the data it needs (line 5 above in **Code Example 3**)


**Code Example 4:**
_from PiMotions/server/motion-detector.py_:
```python {.line-numbers}
# cb is the callback 'send_motion_event'
# when we call the 'send_motion_event' callback (not yet implemented),
# the Pi will send the 'motion-detected' message to the front end.

def boot_motion(cb, exit_func):
    try:
        # initializing MotionDetector with the callback
        md = MotionDetector(cb)
        md.start()
    except:
        e = sys.exc_info()[0]
        exit_func(e)
```

In addition to ```boot_motion```, we have some other utility functions at the bottom of the motion-detector.py file written for us. We'll use these for build out our motion-detecting functionality.

3) The ```start``` method has also been written for us.
put multithreading expl. here

**Code Example 5:**
_from PiMotions/server/motion-detector.py_:
```python {.line-numbers}
class MotionDetector:

    def __init__(self, cb):
        self.cb = cb
        self.camera = Camera()

    def start(self):
        self.camera.start()
        t = Thread(target=self.detector)
        t.daemon = True
        t.start()
```

#### Okay, we're ready to write some code!

We're going to implement the `detector`, `check_for_motion`, and `pix_diff` methods in the `MotionDetector` class. Once we do that, we'll have a working motion-detecting application that leverages the Raspberry Pi.

```python {.line-numbers}
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

```

The completed code is on a branch called `motion-detection-complete`.

You can checkout that branch if you'd like to see a completed version of the code by running `git checkout motion-detection-complete` in your terminal.

### 3. Resin sync

1. Sync your code with your device!
