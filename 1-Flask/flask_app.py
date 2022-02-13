from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)

api = Api(app)

class Users(Resource):

    def get(self):
        return {'name': 'Manoj'}

api.add_resource(Users, '/ggl')

if __name__ == '__main__':
    app.run(debug=True)
