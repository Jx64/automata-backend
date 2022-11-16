from generateAutomata import Automaton
from stepwise import Stepwise

class Automata:

    def __init__(self, word, type) -> None:
        self.word = word
        self.type = type

    def stackRoute(self):
        getStackRoute = list(Automaton().generateAutomata(self.type).read_input_stepwise(self.word))
        stackElements = []
        for element in range(len(self.word)+1):
            stackElements.append(getStackRoute[element].pop())
        return stackElements
    #the method read_input_stepwise(input_str: Any) returns a set, then this function allows get the generator
    # elements and put them into a list
    def nodeRoute(self):
        getElementsInGenerator = list(Automaton().generateAutomata(self.type).read_input_stepwise(self.word))
        nodeElements = []
        for element in range(len(self.word)+1):
            nodeElements.append(getElementsInGenerator[element].pop())
        return nodeElements

    def stepwiseGenerator(self, nodeElements):
        Stepwise().route.clear()
        for i in range(len(self.word)):
            for j in range(1, len(self.word)+1):
                Stepwise().add(self.word[i],nodeElements[i],nodeElements[j])
                break

