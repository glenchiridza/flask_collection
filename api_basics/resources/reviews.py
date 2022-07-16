from flask import jsonify
from flask_restful import Resource


class ReviewList(Resource):
    def get(self):
        return jsonify({'courses': [{'title': 'API basics'}]})


class Review(Resource):
    def get(self, id):
        return jsonify({'title': 'API basics'})

    def put(self, id):
        return jsonify({'title': 'API basics'})

    def delete(self, id):
        return jsonify({'title': 'API basics'})
