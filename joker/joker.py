import json
from random import choice


class Joker:
    def __init__(self):
        self._jokes = json.load(open('/Users/denizulcay/code/local/aws-sample-scripts/resources/jokes/jokes.json', 'r'))

    def tell_joke(self) -> str:
        return choice(self._jokes)
