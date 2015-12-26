"""Handle incoming requests and send back the picture"""
import io

from flask import Flask, send_file, render_template
try:
    import picamera
except:
    print('Camera not found')
    pass
app = Flask(__name__)

@app.route("/picture")
def take_picture():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 1024)
        filename = "temp.jpg"
        camera.capture(filename)
        print open('./images/'+ filename, "w")

# TODO: Take picture on every capture
# TODO: Download picture rather than send picture on mobile.
@app.route("/get_picture")
def get_picture():
    return send_file('temp.jpg')

@app.route("/")
def render_picture():
    return render_template('/show_camera_stream.html')

@app.route("/capture")
def render_capture():
    take_picture()
    return render_template('show_picture.html')
