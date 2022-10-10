from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from automata.fa.nfa import NFA
from automataDesign import Automata

app = Flask(__name__)
CORS(app)

@cross_origin
@app.route('/validate', methods=["GET"])
def automataWord():
    args = request.args.get('word')
    if (args == ""):
        return jsonify({"word": "",
                    "valid": True,
                    "stepwise": []})
    else:
        nonDeterministicFiniteAutomata = NFA(
                                    states={'q0', 'q1', 'q2'},
                                    input_symbols={'a', 'b', 'c'},
                                    transitions={
                                        'q0': {'a': {'q1'}, 'b': {'q2'}, 'c': {'q2'}},
                                        'q1': {'a': {'q1'}},
                                        'q2': {'b': {'q2'}, 'c': {'q2'}}
                                    },
                                    initial_state='q0',
                                    final_states={'q0', 'q1', 'q2'}
                                )   
        
        if nonDeterministicFiniteAutomata.accepts_input(args):
            getElementsInStepwiseGenerator = list(nonDeterministicFiniteAutomata.read_input_stepwise(args))
            routeElements = []
            for element in range(len(args)+1):
                routeElements.append(getElementsInStepwiseGenerator[element].pop())

            newAutomata = Automata(args, True)
                
            return jsonify(newAutomata.automataDesignProcess(routeElements)) 
        else:
            return jsonify({"word": args,
                    "valid": False,
                    "stepwise": []})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
