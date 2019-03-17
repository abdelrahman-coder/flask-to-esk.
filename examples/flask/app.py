from flask import Flask
import os
APP = Flask(__name__)


@APP.route('/')
def hello_world():
    return f'Hello, World from Flask. I am  new{os.getpid()}!\n'



if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
