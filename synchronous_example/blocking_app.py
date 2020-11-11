from time import sleep

from flask import Flask

import config

app = Flask(__name__)

"""
The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) 
that allows only one thread to hold the control of the Python interpreter. 
This means that only one thread can be in a state of execution at any point in time.
"""
@app.route('/')
def hello_world():
    print("does some processing")
    sleep(5)  # blocks the python interpreter
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)
