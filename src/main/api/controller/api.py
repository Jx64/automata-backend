from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from apiMethods import Api
from pushdown import palabras

app = Flask(__name__)
CORS(app)

@cross_origin
@app.route('/NFA/validate', methods=["GET"])
def get_NFAautomata():
    queryString = request.args.get('word')
    api = Api(queryString.lower(), 'NFA')
    return jsonify(api.establishRequestWithAutomata())

@cross_origin
@app.route('/NPDA/validate', methods=["GET"])
def get_NDPAautomata():
    queryString = request.args.get('word')
    api = Api(queryString.lower(), 'NPDA')
    return jsonify(api.establishRequestWithAutomata())
