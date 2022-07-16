import json

from flask import Blueprint, make_response
from flask_restful import (Resource, Api, reqparse, inputs,
                           fields, marshal_with, marshal, url_for)

import models

user_fields = {
    'username': fields.String,
}


class UserList(Resource):
    def __int__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            help='username is required',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'email',
            required=True,
            help='email is required',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'password',
            required=True,
            help='password is required',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'verify_password',
            required=True,
            help='password verification is required',
            location=['form', 'json']
        )
        super(UserList, self).__int__()

    def post(self):
        args = self.reqparse.parse_args()
        if args.get('password') == args.get('verify_password'):
            user = models.User.create_user(**args)
            return marshal(user, user_fields), 201
        return make_response(
            json.dumps({
                'error': 'Password verification failed'
            }), 400)


users_api = Blueprint('resources.users', __name__)
api = Api(users_api)
api.add_resource(
    UserList,
    '/users',
    endpoint='users'
)