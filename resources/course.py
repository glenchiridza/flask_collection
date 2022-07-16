from flask import jsonify,Blueprint
from flask_restful import Resource,Api


class CourseList(Resource):
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