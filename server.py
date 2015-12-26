"""Handle incoming requests and send back the picture"""
import time, os, urllib
from flask import Flask, send_file, render_template
try:
    import picamera
except:
    print('Camera not found')
    pass
app = Flask(__name__)

@app.route("/picture/<filename>")
def take_picture(filename, callback):
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 1024)
        filepath = urllib.unquote(filename)
        print('Take Picture:' + filepath)
        if not os.path.exists(os.path.dirname(filepath + '.jpg')):
            os.makedirs(os.path.dirname(filepath + '.jpg'))
        camera.capture(filepath + '.jpg')
        return callback(filename)

# TODO: Take picture on every capture
# TODO: Download picture rather than send picture on mobile.
@app.route("/get_picture/<filename>")
def get_picture(filename):
    filepath = urllib.unquote(filename)
    return send_file(filepath + '.jpg')

@app.route("/")
def render_picture():
    return render_template('/show_camera_stream.html')

@app.route("/capture")
def render_capture():
    filename = urllib.quote(time.strftime("images/%Y%m%d/%H%M%S"), safe="")
    return take_picture(filename, show_picture)

def show_picture(filename):
    return render_template('show_picture.html', filename=filename)

if __name__ == '__main__':
    # TODO: Don't alays expose to whole internet
    app.debug = True
    app.run(host="0.0.0.0")
