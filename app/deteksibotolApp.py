from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return "Aplikasi Deteksibotol"

if __name__ == '__main__':
    app.run()