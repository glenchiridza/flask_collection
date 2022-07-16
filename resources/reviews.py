from flask import jsonify, Blueprint
from flask_restful import Resource, Api,reqparse,inputs


class ReviewList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'course',
            required=True,
            help='course must be provided',
            location=['form','json']
        )
        self.reqparse.add_argument(
            'rating',
            required=True,
            help='please provide rating',
            location=['form','json'],
            type=inputs.int_range(1,5)
        )
        self.reqparse.add_argument(
            'comment',
            required=False,
            nullable=True,
            default='',
            location=['form','json']
        )
        super(ReviewList, self).__init__()
        
    def get(self):
        return jsonify({'reviews': [{'course': 1, 'rating': 5}]})


class Review(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'course',
            required=True,
            help='course must be provided',
            location=['form','json']
        )
        self.reqparse.add_argument(
            'rating',
            required=True,
            help='please provide rating',
            location=['form','json'],
            type=inputs.int_range(1,5)
        )
        self.reqparse.add_argument(
            'comment',
            required=False,
            nullable=True,
            default='',
            location=['form','json']
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
