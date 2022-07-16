from flask import jsonify,Blueprint
from flask_restful import Resource,Api, reqparse


class CourseList(Resource):
    def __init__(self):

    def get(self):
        return jsonify({'courses': [{'title': 'API basics'}]})


class Course(Resource):
    def get(self, id):
        return jsonify({'title': 'API basics'})

    def put(self, id):
        return jsonify({'title': 'API basics'})

    def delete(self, id):
        return jsonify({'title': 'API basics'})


courses_api = Blueprint('resources.courses',__name__)
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