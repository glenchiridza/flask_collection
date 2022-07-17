from flask import jsonify, Blueprint, abort, url_for
from flask_restful import (Resource, Api, reqparse, inputs, fields,
                           marshal, marshal_with)
from auth import auth
import models

review_fields = {
    'id': fields.Integer,
    'for_course': fields.String,
    'rating': fields.Integer,
    'comment': fields.String(default=''),
    'create_on': fields.DateTime
}


def review_or_404(review_id):
    try:
        review = models.Review.get(models.Review.id == review_id)
    except models.Review.DoesNotExist:
        abort(404)
    else:
        return review


def add_course(review):
    review.for_course = url_for('resources.courses.course', id=review.course.id)
    return review


class ReviewList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'course',
            required=True,
            help='course must be provided',
            location=['form', 'json'],
            type=inputs.positive
        )
        self.reqparse.add_argument(
            'rating',
            required=True,
            help='please provide rating',
            location=['form', 'json'],
            type=inputs.int_range(1, 5)
        )
        self.reqparse.add_argument(
            'comment',
            required=False,
            nullable=True,
            default='',
            location=['form', 'json']
        )
        super(ReviewList, self).__init__()

    def get(self):
        return {'reviews': [
            marshal(add_course(review), review_fields)
            for review in models.Review.select()
        ]}

    @auth.login_required
    def post(self):
        args = self.reqparse.parse_args()
        # the arguments are parsed and output as dictionary
        review = models.Review.create(**args)
        return add_course(review)


class Review(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'course',
            required=True,
            help='course must be provided',
            location=['form', 'json'],
            type=inputs.positive
        )
        self.reqparse.add_argument(
            'rating',
            required=True,
            help='please provide rating',
            location=['form', 'json'],
            type=inputs.int_range(1, 5)
        )
        self.reqparse.add_argument(
            'comment',
            required=False,
            nullable=True,
            default='',
            location=['form', 'json']
        )
        super().__init__()

    @marshal_with(review_fields)
    def get(self, id):
        return add_course(review_or_404(id))

    @auth.login_required
    def put(self, id):
        args = self.reqparse.parse_args()
        review = review_or_404(id)
        query = review.update(**args)
        query.execute()
        review = add_course(review_or_404(id))
        return (review, 200,
                {'location': url_for('resources.reviews.review', id=id)})

    @auth.login_required
    def delete(self, id):
        return jsonify({'course': 1, 'rating': 5})


reviews_api = Blueprint("resources.reviews", __name__)
api = Api(reviews_api)
api.add_resource(
    ReviewList,
    '/reviews',
    endpoint='reviews'
)
api.add_resource(
    Review,
    '/reviews/<int:id>',
    endpoint='review'
)
