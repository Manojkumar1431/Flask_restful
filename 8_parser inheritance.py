from flask import Flask, request
from flask_restful import Api, Resource, reqparse  # import reqparse

app = Flask(__name__)

api = Api(app)
app.config['BUNDLE_ERRORS'] = True

Book_details = {}

add_book_parser = reqparse.RequestParser()

add_book_parser.add_argument("Title", type=str, required=True, location='args', bundle_errors=True)
add_book_parser.add_argument("author", type=str, required=True, dest='Author', location='form')
add_book_parser.add_argument("Price", type=float, help='Price must be in float type', dest='cost', location=['args', 'form'])
add_book_parser.add_argument("quantity", type=int, help="quantity must be integer value", action='append', dest='inventory')
add_book_parser.add_argument("user-agent", type=str, location='headers')

update_book_parser = add_book_parser.copy()

update_book_parser.remove_argument("author")
update_book_parser.remove_argument("Price")

update_book_parser.replace_argument("quantity", type=int)

