"""Handle incoming requests and send back the picture"""
import io

from flask import Flask, Response, send_file, render_template
from time import sleep
from datetime import datetime
from fractions import Fraction
try:
    import picamera
    from camera_pi import Camera
except:
    print('Camera not found')
    pass
app = Flask(__name__)

@app.route("/picture")
def take_picture():
    try:
        with picamera.PiCamera() as camera:
            camera.resolution = (1024, 1024)
            filename = "temp.jpg"
            camera.framerate = Fraction(1, 6)
            camera.shutter_speed = 6000000
            camera.exposure_mode = 'off'
            camera.iso = 800
            # Give the camera a good long time to measure AWB
            # (you may wish to use fixed AWB instead)
            sleep(10)
            camera.capture(filename)
            print open('./images/'+ filename, "w")
            return send_file(filename, mimetype="image/jpg")
    except:
        return send_file('./images/test-image.jpeg')

@app.route("/get_picture")
def get_picture():
    try:
        return send_file('./images/temp.jpg')
    except:
        return send_file('./images/test-image.jpeg')

@app.route("/")
def render_picture():
    return render_template('/show_camera_stream.html')

@app.route("/capture")
def render_capture():
    return render_template('show_picture.html')

def generate_video(camera):
    '''Simulate streaming security-camera video'''
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/video")
def stream_video():
    return Response(generate_video(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # TODO: Don't alays expose to whole internet
    app.debug = True
    app.run(host="0.0.0.0")
