"""Handle incoming requests and send back the picture"""
import io

from flask import Flask, Response, send_file
import picamera
try:
    from camera_pi import Camera
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
    app.run(host="0.0.0.0")
