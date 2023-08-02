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
	@@ -45,4 +60,4 @@ def getNewAcceptedWord(self):
            return newWord[0]

        else:
            return ""
