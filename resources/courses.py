from flask import jsonify, Blueprint
from flask_restful import Resource, Api, reqparse,inputs


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
        return jsonify({'courses': [{'title': 'API basics'}]})


class Course(Resource):
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
