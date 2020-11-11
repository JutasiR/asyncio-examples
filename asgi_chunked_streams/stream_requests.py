import time

import requests

import config

s = requests.Session()


def generate_request():
    print('Sending 1st Msg')
    yield b'hi'
    print('Sleeping.....')
    time.sleep(5)
    print('Sending 2nd Msg')
    yield b'there'


with requests.Session() as client:
    resp = client.post(f'http://{config.HOST}:{config.PORT}', data=generate_request())
    print(resp, resp.text.strip())
