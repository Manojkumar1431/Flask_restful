from flask import Flask, request
from flask_restful import Api, Resource, reqparse  # import reqparse

app = Flask(__name__)

api = Api(app)

Book_details = {}

book_parser = reqparse.RequestParser()  # assigning the command to variable book_parser

'''
type = is used to mention the datatype, so any other datatype other than mentioned throws error
required = when we mention this, we have to definitely use this argument, the arguments where required is not mentioned we can leave them
help = instead of error we can show this message
dest = it is like rename the argument in the output we can choose what name should me mentioned in the output screen instead of given but while while assigning we have to use original
location = in which we need to mention the arguments like form, args, headers
                  form = we need to mention in form 
                  args = we need to mention in the url path
                  headers = it will show the user info 
'''

book_parser.add_argument("Title", type=str, required=True, location='args')
book_parser.add_argument("author", type=str, required=True, dest='Author', location='form')
book_parser.add_argument("Price", type=float, help='Price must be in float type', dest='cost', location=['args', 'form'])
book_parser.add_argument("quantity", type=int, help="quantity must be integer value", action='append', dest='inventory')
book_parser.add_argument("user-agent", type=str, location='headers')

class Book_1(Resource):
    
    def get(self, book_id):
        
        if book_id in Book_details:
            return Book_details[book_id]
        
        return {'Book with '+book_id+' not found'}
    
    def post(self, book_id):
        
        if book_id in Book_details:
            return {'Book with '+book_id+' already exists'}
        
        args = book_parser.parse_args()  # adding the command to args variable
        Book_details[book_id] = args  # assigning args to book_id
        
        return {'Book with'+book_id+' is added'}
    
api.add_resource(Book_1, '/book/<string:book_id>', '/book_info/<string:book_id>')

if __name__ == '__main__':
    app.run(debug=True)
        
    


















