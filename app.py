from flask import Flask

import models
from resources.courses import courses_api

DEBUG = True
HOST = '0.0.0.0'
PORT = 8000

app = Flask(__name__)
app.register_blueprint(courses_api)


@app.route('/')
def index():
    return 'this is home'


if __name__ == "__main__":
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
