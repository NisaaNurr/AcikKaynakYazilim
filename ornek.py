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

    def post(self):
        Il = request.args['Il']
        Sicaklik = request.args['Sicaklik']
        havadurumu = request.args['havadurumu']

	data = pd.read_csv('havadurumu.csv')

        new_data = pd.DataFrame({
            'Il': [Il],
            'Sicaklikk': [Sicaklik],
            'havadurumu': [havadurumu]
        })

        data = data.append(req_data, ignore_index=True)
        data.to_csv('havadurumu.csv', index=False)
        return {'message': 'Record successfully added.'}, 200


class Il(Resource):
    def get(self, Il):
        data = pd.read_csv('havadurumu.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['Il'] == Il:
                return {'data': entry}, 200
        return {'message': 'Ilin hava durumu bilgisi bulunamadı!'}, 404

# Add URL endpoints
api.add_resource(Users, '/users')
api.add_resource(Name, '/<string:Il>')

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=6767)
   app.run()
