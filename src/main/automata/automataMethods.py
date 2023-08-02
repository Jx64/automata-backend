from main.automata.generateAutomata import Automaton
from main.datatypes.stepwise import Stepwise

class Automata:

    def __init__(self, word) -> None:
        self.word = word

    #the method read_input_stepwise(input_str: Any) returns a set, then this function allows get the generator
    # elements and put them into a list
    def nodeRoute(self):
        getElementsInGenerator = list(Automaton().generateAutomata().read_input_stepwise(self.word))
        nodeElements = []
        for element in range(len(self.word)+1):
            nodeElements.append(getElementsInGenerator[element].pop())
