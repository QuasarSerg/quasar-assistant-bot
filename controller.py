from flask import Flask
from threading import Thread

app = Flask('app')


@app.route('/')
def satus():
    return 'OK'


def run_web_service():
    Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()
