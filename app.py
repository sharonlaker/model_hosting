from flask import Flask,request
from flask_restful import Resource, Api
import pickle
import pandas as pd
from flask_cors import CORS


app = Flask(__name__)
#
CORS(app)
# creating an API object
api = Api(app)

#prediction api call
class prediction(Resource):
    def get(self,prediction_duration):
        #prediction_duration = request.args.get('prediction duration')
        print(prediction_duration)
        # Let's load the package
        prediction_duration = [int(prediction_duration)]
        df = pd.DataFrame(prediction_duration, columns=['Timestamp'])
        model = pickle.load(open('sarima.pkl', 'rb'))
        prediction = model.predict(df)
        prediction = int(prediction[0])
        return str(prediction)

#data api
class getData(Resource):
    def get(self):
            df1 = pd.read_excel('fake3_1.xlsx')
            # df =  df.rename({'Timestamp': 'prediction_duration', 'Actual Sales': 'sale'}, axis=1)  # rename columns
            #print(df.head())
            #out = {'key':str}
            res = df1.to_json(orient='records')
            #print( res)
            return res

#
api.add_resource(getData, '/api')
api.add_resource(prediction, '/prediction/<int:budget>')

if __name__ == '__main__':
    app.run(debug=True)