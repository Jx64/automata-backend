from typing import List

class Stepwise:
    edge: str
    source: str
    target: str
    route = []

    def __init__(self) -> None:
        pass

    def add(self, edge, source, target):
        Stepwise.route.append({"source": source, "target": target, "edge": edge})

    def get(self):
        return Stepwise.route
