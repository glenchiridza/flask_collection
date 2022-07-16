from flask import jsonify, Blueprint
from flask_restful import Resource, Api, reqparse, inputs, fields

import models

review_fields = {
    'id': fields.Integer,
    'for_course': fields.String,
    'rating': fields.Integer,
    'comment': fields.String(default=''),
    'create_on': fields.DateTime
}


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
        return jsonify({'reviews': [{'course': 1, 'rating': 5}]})

    def post(self):
        args = self.reqparse.parse_args()
        # the arguments are parsed and output as dictionary
        models.Review.create(**args)
        return jsonify({'reviews': [{'course': 1, 'rating': 5}]})


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

    def get(self, id):
        return jsonify({'course': 1, 'rating': 5})

    def put(self, id):
        return jsonify({'course': 1, 'rating': 5})

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
