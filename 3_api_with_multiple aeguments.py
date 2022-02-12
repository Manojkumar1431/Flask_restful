from flask import Flask
from flask_restful import Resource, Api  # we need to import flask_restful

app = Flask(__name__)

api = Api(app)

class Employee(Resource):
    def get(self, emp_id, name):
        return {'Employee ID': emp_id, 'Name ': name}

api.add_resource(Employee, '/emp/<int:emp_id>/<string:name>/')

if __name__ == '__main__':
    app.run(debug=True)