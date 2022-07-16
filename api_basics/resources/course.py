from flask import jsonify
from flask_restful import Resource


class CourseList(Resource):
    def get(self):
        return jsonify({'courses': [{'title': 'API basics'}]})


class Course(Resource):
    def get(self):

