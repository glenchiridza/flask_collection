from flask import Flask
import config
import models
from resources.courses import courses_api
from resources.reviews import reviews_api

app = Flask(__name__)
app.register_blueprint(courses_api)
app.register_blueprint(reviews_api, url_prefix='/api/v1')


@app.route('/')
def index():
    return 'this is home'


if __name__ == "__main__":
    models.initialize()
    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
