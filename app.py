from flask import Flask, g, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_ipaddr

import config
import models
from resources.courses import courses_api
from resources.reviews import reviews_api
from resources.users import users_api
from auth import auth

app = Flask(__name__)
app.register_blueprint(courses_api)
app.register_blueprint(reviews_api, url_prefix='/api/v1')
app.register_blueprint(users_api, url_prefix='/api/v1')


@app.route('/')
def index():
    return 'this is home'


@app.route('/api/v1/users/token', methods=['GET'])
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    # decode it to ascii to make it safe to send across
    return jsonify({'token': token.decode('ascii')})


if __name__ == "__main__":
    models.initialize()
    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
