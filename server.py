"""Handle incoming requests and send back the picture"""
import time
from flask import Flask, send_file, render_template
try:
    import picamera
except:
    print('Camera not found')
    pass
app = Flask(__name__)

@app.route("/picture")
def take_picture(filename):
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 1024)
        camera.capture(filename)

# TODO: Take picture on every capture
# TODO: Download picture rather than send picture on mobile.
@app.route("/get_picture")
def get_picture(filename):
    return send_file(filename)

@app.route("/")
def render_picture():
    return render_template('/show_camera_stream.html')

@app.route("/capture")
def render_capture():
    filename = time.strftime("%Y%m%d-%H%M%S") + ".jpg"
    take_picture(filename)
    return render_template('show_picture.html', filename=filename)

if __name__ == '__main__':
    # TODO: Don't alays expose to whole internet
    app.debug = True
    app.run(host="0.0.0.0")
