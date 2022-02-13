from flask import Flask
from flask_restful import Resource, Api  # we need to import flask_restful

app = Flask(__name__)

api = Api(app)  # we are giving flask app as input to the restfull service so,it will take care of the GET/POST requests

# we need to give Resource as an argument in class as, Resource will take care pf requests received and respond as based on the request
class Helloworld(Resource):
    def get(self):
        return {'message': 'Welcome buddy'}  # NOTE: flask restfull only return in json format as response if we need to confiure HTML/XML/etc we need to provide keywords

    def post(self):
        return {'message': 'This is a POST request'}

    def put(self):
        return {'message': 'This is a PUT request'}

    def delete(self):
        return {'Message': 'This is a Delete request'}

api.add_resource(Helloworld, '/')  # we are routing the response through this command api.add_resource(classname, url path) same like @app.route decorator

if __name__ == '__main__':
    app.run(debug=True)  # here we are setting up the debug mode so any changes we make in the code will automatically get reflected in the result




