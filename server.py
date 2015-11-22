"""Handle incoming requests and send back the picture"""
import os

from flask import Flask, send_file
import picamera

app = Flask(__name__)
app.debug = os.env.get("WEB_PI_CAM_DEBUG", True)

@app.route("/picture")
def take_picture():
    with picamera.PiCamera() as camera:
        filename = "temp.jpg"
        camera.capture(filename)
        send_file(filename, mimetype="image/jpg")

if __name__ == '__main__':
    app.run()
