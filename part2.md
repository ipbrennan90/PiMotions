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
At the beginning of the function, we read an image to a BytesIO stream (lines 2 and 3). We move to the start of the stream (line 4), and then load a PIL Image object from the stream in line 5. We then `load` the PIL Image object, which reads the image data and returns a pixel access object that we can use to read pixels.

If we wanted to, we could access a specific pixel in the `im_buffer` by providing the pixel coordinates (ex `im_buffer[x,y]`), which will return a tuple (a collection) of RGB values.

```python
  x = 10
  y = 12
  print(image_buffer[x,y])
```
would return something like ```(10,148,218)```, representing R, G, and B values respectively.

In case you were wondering, the color rgb(10, 232, 218) looks like <span style="color:#0ae8da;">this!</span>

With an understanding of our camera under our belts, let's take a quick tour through our server.py file.

### server.py

Open `server.py` in your text editor.

We're using sockets in this application, meaning that we're using real-time event-based communication between our Pi and our web app. If you don't know what that means, don't worry!

At a high level, you can think about sockets like a line of communication that stays open between the web app and the Pi. The web app and the Pi are listening on this line of communication for different events.

When the web app emits the 'set-threshold' event, like in the code example excerpted below, the Pi will take certain actions, like calling the function `set_threshold()` on line 3. (We'll get into what the threshold is in the next section). The Pi then emits a message of its own back to the web app (line 4), sending a ```"threshold"``` message with some data for the web app to display.

_from PiMotions/server/server.py_:
```python {.line-numbers}
@socketio.on('set-threshold')
def set_motion_threshold(threshold):
    set_threshold(threshold)
    emit('threshold', {'threshold': threshold})
```

Now that we know what our camera looks like and how the real-time communication works between the Pi and the web app, let's write some motion-detecting code of our own!

### 2. Motion-detection magic

All of our code is going to be written in motion-detector.py. When we get the code we need written in this file, our front end will magically work!



1.

### 3. Resin sync

1.
