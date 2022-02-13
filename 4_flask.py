from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

#  created a Dictionary
emp_data = {
    100: {'name': 'Manoj', 'Role': 'ASE', 'salary': '4.5L'},
    200: {'name': 'Mintu', 'Role': 'SE', 'salary': '6L'}
}

class Employee(Resource):
    def get(self, emp_id):  # give dictionary key as argument to the function
        return emp_data[emp_id]

api.add_resource(Employee, '/emp_data/<int:emp_id>')

if __name__ == '__main__':
    app.run(debug=True)
