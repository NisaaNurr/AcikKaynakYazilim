from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        data = pd.read_csv('havadurumu.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200

    def post(self):
        il=request.args['İl']
        sıcaklık=request.args['sıcaklık']
        havadurumu=request.args['havadurumu']

        req_data = pd.DataFrame({
            'İl'    : ['İl'],
            'sıcaklık'    : ['sıcaklık'],
            'havadurumu'      : ['havadurmu']

        })
        data = pd.read_csv('users.csv')
        #data = pd.concat([data, req_data], ignore_index=True)
        data=data.append(req_data,ignore_index=True)
        data.to_csv('users.csv', index=False)
        return {'message' : 'Record successfully added.'}, 200


class Name(Resource):
    def get(self,name):
        data = pd.read_csv('havadurumu.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['name'] == name :
                return {'data' : entry}, 200
        return {'message' : 'İlin hava durumu bilgisi bulunamadı ! '}, 404
# Add URL endpoints
api.add_resource(havadurumu, '/users')
api.add_resource(İl, '/<string:İl>')


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=6767)
    app.run()
