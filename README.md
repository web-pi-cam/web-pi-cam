# Web Pi Cam
Interact with the [Rasberry Pi Camera module](https://www.raspberrypi.org/products/camera-module/) through the web.

## Installation
Make sure you have `pip` [installed](https://pip.pypa.io/en/stable/installing/). Using [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.org/en/latest/) is recommended to isolate environments.

To install dependencies:

`pip install -r requirements.txt`

To run the server:

`python server.py`

Navigate to `http://localhost:5000/picture` to see it in action.

This only works if you are running the server on a Rasberry Pi with the Camera module installed. If you try to run it on a local Linux or Macbook, you will see something awful like this:

```
File "server.py", line 5, in <module>
  import picamera
  ...
OSError: dlopen(libmmal.so, 6): image not found
```

## Endpoint
* `/picture` - take your picture

## Contributing
Send pull requests, post issues, feature requests, etc. See [Github guide to contributing](https://guides.github.com/activities/contributing-to-open-source/) for ideas and guidelines.

## License
[MIT](https://opensource.org/licenses/MIT)
