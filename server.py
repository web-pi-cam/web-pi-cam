"""Handle incoming requests and send back the picture"""
from flask import Flask, send_file
import picamera

app = Flask(__name__)

@app.route("/picture")
def take_picture():
    with picamera.PiCamera() as camera:
        filename = "temp.jpg"
        camera.capture(filename)
        send_file(filename, mimetype="image/jpg")
