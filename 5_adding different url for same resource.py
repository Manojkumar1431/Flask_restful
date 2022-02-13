from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

sales_data = {
    100: {'name': 'Akhil', 'Role': 'sales', 'salary': '5L'},
    200: {'name': 'Nikhil', 'Role': 'AEO', 'salary': '6.5L'}
}
eng_data = {
    100: {'name': 'Manoj', 'Role': 'ASE', 'salary': '7L'},
    200: {'name': 'Mintu', 'Role': 'SE', 'salary': '8L'}
}

class Eng_emp(Resource):
    def get(self, e_id):
        return eng_data[e_id]

class Sales_emp(Resource):
    def get(self, s_id):
        return sales_data[s_id]

api.add_resource(Eng_emp,
                 '/eng_emp/<int:e_id>', '/engg/<int:e_id>')  # here two urls are added for same resource, it will work

api.add_resource(Sales_emp,
                 '/sales_emp/<int:s_id>', '/sales/<int:s_id>')

'''
# other method to add urls for same resources

api.add_resource(Eng_emp, '/eng_emp/<int:e_id>', endpoint='eng_1')
api.add_resource(Eng_emp, '/engg/<int:e_id>', endpoint='eng_2')  # here if you observe the two url's mapped to same resource we need to mention endpoint keyword in order to tell that they are same with different ids
'''


if __name__ == '__main__':
    app.run(debug=True)