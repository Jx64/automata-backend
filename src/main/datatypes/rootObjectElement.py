from typing import List
from ..stepwise import Stepwise


class RootObjectElement:
    stepwise: List[Stepwise]
    valid: bool
    word: str

    def __init__(self, stepwise: List[Stepwise], valid: bool, word: str) -> None:
        self.stepwise = stepwise
        self.valid = valid
        self.word = word

    def get(self):
        return {"stepwise": self.stepwise, "valid": self.valid, "word": self.word}
