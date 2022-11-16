from automata.fa.nfa import NFA
from automata.pda.npda import NPDA

class Automaton:

    #This function was made in case of refactoring
    #Example Automaton(self, args[])
    def __init__(self) -> None:
        pass

    #This function can't be delete or modified, at least that the programmer gonna edit the init function
    #In case of edit take a look in this format: generateAutomata(self, List[args], args)
    def generateAutomata(self, type):
        if type == 'NFA':
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
        if type == 'NPDA':
            return NPDA(
                    states={'q0', 'q1', 'q2'},
                    input_symbols={'a', 'b'},
                    stack_symbols={'A', 'B', '#'},
                    transitions={
                        'q0': {
                            '': {
                                '#': {('q2', '#')},
                            },
                            'a': {
                                '#': {('q0', ('A', '#'))}, 
                                'A': {
                                    ('q0', ('A', 'A')), 
                                    ('q1', ''), 
                                },
                                'B': {('q0', ('A', 'B'))},  
                            },
                            'b': {
                                '#': {('q0', ('B', '#'))}, 
                                'A': {('q0', ('B', 'A'))}, 
                                'B': {
                                    ('q0', ('B', 'B')),
                                    ('q1', ''), 
                                },
                            },
                        },
                        'q1': {
                            '': {'#': {('q2', '#')}}, 
                            'a': {'A': {('q1', '')}}, 
                            'b': {'B': {('q1', '')}}, 
                        },
                    },
                    initial_state='q0',
                    initial_stack_symbol='#',
                    final_states={'q2'},
                    acceptance_mode='final_state'
                )

    def isValid(self, word, type):
        if Automaton().generateAutomata(type).accepts_input(word):
            return True
        else:
            return False

