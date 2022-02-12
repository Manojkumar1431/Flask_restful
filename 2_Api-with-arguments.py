from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class Helloworld_1(Resource):

    def get(self, name):  # argument was added
        return {'message': 'Hello ' + name}

api.add_resource(Helloworld_1, '/greeting/<string:name>')  # creating the argument with datatype

if __name__ == '__main__':
    app.run(debug=True)