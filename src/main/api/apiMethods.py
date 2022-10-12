from main.automata.automataMethods import Automata
from main.automata.generateAutomata import Automaton
from main.datatypes.rootObjectElement import RootObjectElement
from main.datatypes.stepwise import Stepwise
import re

class Api:

    def __init__(self, queryString) -> None:
        self.queryString = queryString

    def setRejectedConnection(self):
        return "Reject connection"

    def establishRequestWithAutomata(self):
        if self.queryString == '':
            return Api(self.queryString).getEmptyQueryStringJSON()
        else:
            return Api(self.queryString).getJSON()
        
    def getEmptyQueryStringJSON(self):
        return {"stepwise": [], "valid": True, "word": self.queryString}

    def getJSON(self):
        if Automaton().isValid(self.queryString):
            Automata(self.queryString).stepwiseGenerator(Automata(self.queryString).nodeRoute())
            return RootObjectElement(Stepwise().get(), Automaton().isValid(self.queryString), self.queryString).get()
        else:
            newQueryString = Api(self.queryString).getNewAcceptedWord()
            Automata(newQueryString).stepwiseGenerator(Automata(newQueryString).nodeRoute())
            return RootObjectElement(Stepwise().get(), False, self.queryString).get()

    #This functions divides the queryString and get a new one, this new one is a accepted word
    #would help for generate a stepwise for a non-accepted word
    #Example: "bbc823xcbb", the function returns the word "bbc" and generate a stepwise of this word
    def getNewAcceptedWord(self):
        language_a = "[b-z]|[0-9]"
        language_b = "a|[d-z]|[0-9]"
        if self.queryString[0] == 'a':
            newWord = re.split(language_a, self.queryString)
            return newWord[0]
        
        elif self.queryString[0] == 'b' or self.queryString == 'c':
            newWord = re.split(language_b, self.queryString)
            return newWord[0]

        else:
            return ""