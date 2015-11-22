"""Handle incoming requests and send back the picture"""
import os

from flask import Flask, send_file
try:
    import picamera
except:
    pass

app = Flask(__name__)

@app.route("/picture")
def take_picture():
    try:
        with picamera.PiCamera() as camera:
            filename = "temp.jpg"
            camera.capture(filename)
            return send_file(filename, mimetype="image/jpg")
    except:
        return send_file('/images/test-image.jpg')

@app.route("/")
def render_picture():
    return render_template('/templates/show_camera_stream.html', picture='/picture')

if __name__ == '__main__':
    # TODO: Don't alays expose to whole internet
    app.run(host="0.0.0.0")
