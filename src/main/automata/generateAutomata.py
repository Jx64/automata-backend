from automata.fa.nfa import NFA

class Automaton:

    #This function was made in case of refactoring
    #Example Automaton(self, args[])
    def __init__(self) -> None:
        pass

    #This function can't be delete or modified, at least that the programmer gonna edit the init function
    #In case of edit take a look in this format: generateAutomata(self, List[args], args)
    def generateAutomata(self):
        return NFA(states={'q0', 'q1', 'q2'},
                input_symbols={'a', 'b', 'c'},
                transitions={
                            'q0': {'a': {'q1'}, 'b': {'q2'}, 'c': {'q2'}},
                            'q1': {'a': {'q1'}},
                            'q2': {'b': {'q2'}, 'c': {'q2'}}
                            },
                initial_state='q0',
                final_states={'q0', 'q1', 'q2'}
                )

    def isValid(self, word):
        if Automaton().generateAutomata().accepts_input(word):
            return True
        else:
            return False
