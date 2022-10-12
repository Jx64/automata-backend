from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from main.api.apiMethods import Api

app = Flask(__name__)
CORS(app)

@cross_origin
@app.route('/validate', methods=["GET"])
def get_automata():
    queryString = request.args.get('word')
    api = Api(queryString.lower())
    return jsonify(api.establishRequestWithAutomata())
