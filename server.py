"""Handle incoming requests and send back the picture"""
import os

from flask import Flask, send_file
import picamera

app = Flask(__name__)

@app.route("/picture")
def take_picture():
    with picamera.PiCamera() as camera:
        filename = "temp.jpg"
        camera.capture(filename)
        return send_file(filename, mimetype="image/jpg")

if __name__ == '__main__':
    # TODO: Don't alays expose to whole internet
    app.run(host="0.0.0.0")
