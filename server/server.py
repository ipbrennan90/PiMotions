from flask import Flask, Response, send_file, json, request, copy_current_request_context
import logging
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit
from motion_detector import boot_motion, stop_detector, start_detector, set_sensitivity, set_threshold, get_threshold, get_sensitivity
from camera import Camera
import eventlet 

eventlet.monkey_patch()

RUN_CAM = False
ENTROPY_SAMPLE = []


app = Flask(__name__)
CORS(app)
# allowing all origins for development purposes, please adjust this if you are going to run this in production mode
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")
camera = Camera()

@app.route('/take')
def take_picture():
    img_str, _ = camera.capture_b64_image()
    response = Response(
        response = json.dumps({
            'src': img_str
        }),
        status = 200,
        mimetype='application/json'
    )
    return response

@socketio.on('motion-start')
def check_motion():
    @copy_current_request_context
    def send_motion_event(pixChanged, motion_detected):
        emit('motion-data', {'pixChanged': pixChanged, 'motion': motion_detected})

    @copy_current_request_context
    def motion_exit(e):
        logging.exception(e)
        emit('motion-detector-exit', {'exit': 'there was an error in the detector'})
    start_detector()
    boot_motion(send_motion_event, motion_exit)

    
@socketio.on('set-threshold')
def set_motion_threshold(threshold):
    set_threshold(threshold)
    emit('threshold', {'threshold': threshold})

@socketio.on('set-sensitivity')
def set_motion_threshold(sensitivity):
    set_sensitivity(sensitivity)
    emit('sensitivity', {'sensitivity': sensitivity})

@socketio.on('stop-cam')
def stop():
    stop_detector()

@socketio.on('disconnect')
def diconnect():
    stop_detector()

@socketio.on('connect')
def connect():
    threshold = get_threshold()
    sensitivity = get_sensitivity()
    emit('threshold', {'threshold': threshold})
    emit('sensitivity', {'sensitivity': sensitivity})
    
    
        

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=80)
