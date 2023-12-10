from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        data = pd.read_csv('havadurumu.csv')
        data = data.to_dict('records')
        return {'data': data}, 200

        data = pd.read_csv('havadurumu.csv')

    def post(self):
        il = request.args['il']
        sicaklik = request.args['sicaklik']
        havadurumu = request.args['havadurumu']

        new_data = pd.DataFrame({
            'il': [il],
            'sicaklikk': [sicaklik],
            'havadurumu': [havadurumu]
        })
        data = data.append(new_data, ignore_index=True)
        data.to_csv('users.csv', index=False)
        return {'message': 'Record successfully added.'}, 200

class Name(Resource):
    def get(self, name):
        data = pd.read_csv('havadurumu.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['name'] == name:
                return {'data': entry}, 200
        return {'message': 'ilin hava durumu bilgisi bulunamadı!'}, 404

# Add URL endpoints
api.add_resource(Users, '/users')
api.add_resource(Name, '/<string:name>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=6767)
    app.run()
