from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from automata.fa.nfa import NFA
from automataDesign import Automata

app = Flask(__name__)
CORS(app)

@cross_origin
@app.route('/validate/word=', methods=['GET'])
def emptyWord():
    return jsonify({"word": "",
                    "valid": True,
                    "stepwise": []})

@cross_origin
@app.route('/validate/word=<string:word>', methods=["GET"])
def automataWord(word):
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
    getElementsInStepwiseGenerator = list(nonDeterministicFiniteAutomata.read_input_stepwise(word))
    routeElements = []
    for element in range(len(word)+1):
        routeElements.append(getElementsInStepwiseGenerator[element].pop())

    valid = None
    if nonDeterministicFiniteAutomata.accepts_input(word):
        valid = False
    else:
        valid = True
    validate = Automata(word, valid)

    return jsonify(validate.automataDesignProcess(routeElements)) 

if __name__ == '__main__':
    app.run(debug=True, port=4000)
