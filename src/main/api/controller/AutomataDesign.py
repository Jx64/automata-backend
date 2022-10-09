from automata.fa.nfa import NFA

class Automata:
    word: str

    def __init__(self, word, valid):
        self.word = word
        self.valid = valid
            
    def automataDesignProcess(self, routeElements):
        route = []
        for i in range(len(self.word)):
            for j in range(1, len(self.word)+1):
                route.append({"source": routeElements[i], "target": routeElements[j], "edge": self.word[i]})
                break
    
        automatat = {"word": self.word,
                    "valid": self.valid,}

        automatat.update({"stepwise": route})

        return automatat
