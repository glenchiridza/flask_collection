from flask import jsonify, Blueprint, url_for, abort
from flask_restful import (Resource, Api, reqparse, inputs, fields,
                           marshal, marshal_with)
from auth import auth
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


def course_or_404(course_id):
    try:
        course = models.Course.get(models.Course.id == course_id)
    except models.Course.DoesNotExist:
        abort(404)
    else:
        return course


def add_reviews(course):
    course.reviews = [url_for('resources.reviews.review', id=review.id)
                      for review in course.review_set]
    return course


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
        courses = [marshal(add_reviews(course), course_fields)
                   for course in models.Course.select()]  # retreive all
        return {'courses': courses}

    @auth.login_required
    @marshal_with(course_fields)
    def post(self):
        args = self.reqparse.parse_args()
        course = models.Course.create(**args)
        return (add_reviews(course), 201,
                {'location': url_for('resources.courses.course', id=course.id)})


class Course(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title',
            required=True,
            help='course title is required',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'url',
            required=True,
            help='course url is required',
            location=['form', 'json'],
            type=inputs.url
        )
        super().__init__()

    @marshal_with(course_fields)
    def get(self, id):
        return add_reviews(course_or_404(id))

    @marshal_with(course_fields)
    @auth.login_required
    def put(self, id):
        args = self.reqparse.parse_args()
        query = models.Course.update(**args).where(models.Course.id == id)
        query.execute()
        return (add_reviews(models.Course.get(models.Course.id == id)), 200,
                {'location': url_for('resources.courses.course', id=id)})

    @auth.login_required
    def delete(self, id):
        query = models.Course.delete().where(models.Course.id == id)
        query.execute()
        return ('', 204,
                {'locations': url_for('resources.courses.courses')})


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
