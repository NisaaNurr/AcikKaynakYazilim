from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Havadurumu(Resource):
    def get(self):
        data = pd.read_csv('havadurumu.csv')
        data = data.to_dict('records')
        return {'data': data}, 200


    def post(self):
        il = request.args['il']
        sicaklik = request.args['sicaklik']
        havadurumu = request.args['havadurumu']

        data = pd.read_csv('havadurumu.csv')

        new_data = pd.DataFrame({
            'il': [il],
            'sicaklikk': [sicaklik],
            'havadurumu': [havadurumu]
        })
        data = data.append(new_data, ignore_index=True)
        data.to_csv('users.csv', index=False)
        return {'message': 'Record successfully added.'}, 200

class Il(Resource):
    def get(self, il):
        data = pd.read_csv('havadurumu.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['il'] == il:
                return {'data': entry}, 200
        return {'message': 'ilin havadurumu bilgileri bulunamadi'}, 404

# Add URL endpoints
api.add_resource(Havadurumu, '/havadurumu')
api.add_resource(Il, '/il/<string:il>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=6767)
    app.run()
