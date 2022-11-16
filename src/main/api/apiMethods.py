from automataMethods import Automata
from generateAutomata import Automaton
from rootObjectElement import RootObjectElement
from stepwise import Stepwise
import re

class Api:

    def __init__(self, queryString, type) -> None:
        self.queryString = queryString
        self.type = type

    def setRejectedConnection(self):
        return "Reject connection"

    def establishRequestWithAutomata(self):
        if self.queryString == '':
            return Api(self.queryString, self.type).getEmptyQueryStringJSON()
        else:
            return Api(self.queryString, self.type).getJSON()
        
    def getEmptyQueryStringJSON(self):
        if self.type == 'NFA':
            return {"stepwise": [], "valid": True, "word": self.queryString}
        else:
            return {{"stepwise": [], "valid": True, "word": self.queryString, 'stack': []}}

    def getJSON(self):
        if self.type == 'NFA':
            if Automaton().isValid(self.queryString, self.type):
                Automata(self.queryString, self.type).stepwiseGenerator(Automata(self.queryString, self.type).nodeRoute())
                return RootObjectElement(Stepwise().get(), Automaton().isValid(self.queryString, self.type), self.queryString).get()
            else:
                newQueryString = Api(self.queryString, self.type).getNewAcceptedWord()
                Automata(newQueryString, self.type).stepwiseGenerator(Automata(newQueryString, self.type).nodeRoute())
                return RootObjectElement(Stepwise().get(), False, self.queryString).get()
        if self.type == 'NPDA':
            if Automaton().isValid(self.queryString, self.type):
                Automata(self.queryString, self.type).stepwiseGenerator(Automata(self.queryString, self.type).nodeRoute())
                return RootObjectElement(Stepwise().get(), Automaton().isValid(self.queryString, self.type), self.queryString).get()
            else:
                newQueryString = Api(self.queryString, self.type).getNewAcceptedWord()
                Automata(newQueryString, self.type).stepwiseGenerator(Automata(newQueryString, self.type).nodeRoute())
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
