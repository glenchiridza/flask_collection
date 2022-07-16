from flask import jsonify, Blueprint
from flask_restful import Resource, Api, reqparse,inputs,fields

import models

# using reqparse to specify how the input looks like

# using dictionary to specify how the output looks like ,and
# fields to specify the data type

course_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'url': fields.String,  # here we are using string because we are not returning an endpoint to another url,
    # but rather we jus want to get the url that was saved in db
    'reviews': fields.List(fields.String)
}


class CourseList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title',
            required=True,
            help='course title must be provided',
            location=['form', 'json'],  # look for data in form encoded or json encoded data,

        )
        self.reqparse.add_argument(
            'url',
            required=True,
            help='course url must be provided',
            location=['form', 'json'],
            type=inputs.url
        )
        super().__init__()  # make sure the standard setup goes ahead and happen

    def get(self):
        return jsonify({'courses': [{'title': 'API basics'}]})

    def post(self):
        args = self.reqparse.parse_args()
        models.Course.create(**args)
        return jsonify({'courses': [{'title': 'API basics'}]})


class Course(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title',
            required=True,
            help='course title is required',
            location =['form','json']
        )
        self.reqparse.add_argument(
            'url',
            required=True,
            help='course url is required',
            location = ['form','json'],
            type=inputs.url
        )
        super().__init__()

    def get(self, id):
        return jsonify({'title': 'API basics'})

    def put(self, id):

        return jsonify({'title': 'API basics'})

    def delete(self, id):
        return jsonify({'title': 'API basics'})


courses_api = Blueprint('resources.courses', __name__)
api = Api(courses_api)
api.add_resource(
    CourseList,
    '/api/v1/courses',
    endpoint='courses'
)
api.add_resource(
    Course,
    '/api/v1/courses/<int:id>',
    endpoint='course'
)
