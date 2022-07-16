from flask import Blueprint
from flask_restful import (Resource, Api, reqparse, inputs,
                           fields, marshal_with, marshal, url_for)

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
            location=['form','json']
        )
        self.reqparse.add_argument(
            'verify_password',
            required=True,
            help='password verification is required',
            location=['form', 'json']
        )
        super(UserList, self).__int__()


users_api = Blueprint('resources.users', __name__)
api = Api(users_api)
api.add_resource(
    UserList,
    '/users',
    endpoint='users'
)
