import re
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from main.datatypes.rootObjectElement import RootObjectElement
from main.datatypes.stepwise import Stepwise
from main.automata.generateAutomata import Automaton
from main.automata.automataMethods import Automata

app = Flask(__name__)
CORS(app)

@cross_origin
@app.route('/validate', methods=["GET"])
def automataWord():
    args = request.args.get('word')
    args.lower()
    if args == "":
        return jsonify({"stepwise": [], "valid": True, "word": args})
    else:
        if Automaton().isValid(args):
            newAutomata = Automata(args)
            newAutomata.stepwiseGenerator(newAutomata.nodeRoute())
            roe = RootObjectElement(Stepwise().get(), True, args)
            return jsonify(roe.get())

        else:
            if args[0] == 'a':
                newArgs = re.split("[b-z]|[0-9]", args)
                newAutomata = Automata(newArgs[0])
                newAutomata.stepwiseGenerator(newAutomata.nodeRoute())
                roe = RootObjectElement(Stepwise().get(), False, args)
                return jsonify(roe.get())
            elif args[0] == 'b' or args[0] == 'c':
                newArgs = re.split("a|[d-z]|[0-9]", args)
                newAutomata = Automata(newArgs[0])
                newAutomata.stepwiseGenerator(newAutomata.nodeRoute())
                roe = RootObjectElement(Stepwise().get(), False, args)
                return jsonify(roe.get())
            else:
                return jsonify({"stepwise": [], "valid": False, "word": args})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
