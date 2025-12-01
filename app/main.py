from flask import Flask
from flask_restful import Api, Resource, reqparse
from model import predict_class

app = Flask(__name__)
api = Api()

class Main(Resource):
    def get(self):
        return {"info": "News AI Detector API"}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("text", type=str, required=True)
        args = parser.parse_args()
        text = args['text']
        prediction = predict_class(text)
        return prediction

api.add_resource(Main, "/api/main")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host='127.0.0.1')

