from flask import Flask

DEBUG = True
HOST = '0.0.0.0'
PORT = 8000

app = Flask(__name__)


@app.route('/')
def index():
    return 'this is home'


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
