from flask import Flask, request
from flask_restful import Api, Resource, reqparse  # import reqparse

app = Flask(__name__)

api = Api(app)

Book_details = {}

book_parser = reqparse.RequestParser()

# book_parser.add_argument("Title", type=str, required=True, location='args')
book_parser.add_argument("author", type=str, required=True, dest='Author', location='form')
book_parser.add_argument("Price", type=float, help='Price must be in float type', dest='cost', location=['args', 'form'])
book_parser.add_argument("quantity", type=int, help="quantity must be integer value", action='append', dest='inventory', location='headers')

class Book_1(Resource):
    
    def get(self, book_id):
        
        if book_id in Book_details:
            return Book_details[book_id]
        
        return {'Book with '+book_id+' not found'}
    
    def post(self, book_id):
        
        if book_id in Book_details:
            return {'Book with '+book_id+' already exists'}
        
        args = book_parser.parse_args()
        Book_details[book_id] = args
        
        return {'Book with'+book_id+' is added'}
    
api.add_resource(Book_1, '/book/<string:book_id>', '/book_info/<string:book_id>')

if __name__ == '__main__':
    app.run(debug=True)
        
    


















