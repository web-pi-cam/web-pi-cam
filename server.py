"""Handle incoming requests and send back the picture"""
import io

from flask import Flask, Response, send_file, render_template
from time import sleep
from fractions import Fraction
try:
    import picamera
    from camera_pi import Camera
except:
    print('Camera not found')
    pass
app = Flask(__name__)
stream = io.BytesIO()
@app.route("/picture")
def take_picture():
    try:
        with picamera.PiCamera() as camera:
            filename = "temp.jpg"
            camera.capture(filename)
            return send_file(filename, mimetype="image/jpg")
    except:
        return send_file('./images/test-image.jpeg')

@app.route("/")
def render_picture():
    return render_template('/show_camera_stream.html')

def generate_video(camera):
    camera.start_recording(stream, format='h264', quality=23)
    camera.wait_recording(15)
    camera.stop_recording()
    # '''Simulate streaming security-camera video'''
    # while True:
    #     frame = camera.get_frame()
    #     yield (b'--frame\r\n'
    #            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/video")
def stream_video():
    with picamera.PiCamera() as camera:
        return generate_video(camera)
    # return Response(generate_video(Camera()),
    #                 mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # TODO: Don't alays expose to whole internet
    app.debug = True
    app.run(host="0.0.0.0")
