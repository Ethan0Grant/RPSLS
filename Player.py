
from unicodedata import name

class Player:
    def __init__(self):
        self.score = 0
        self.name = None
        self.move = "Invalid"
        self.gesture = ['rock', 'paper', 'scissors', 'lizard', 'spock']


    def point(self):
        self.score = self.score + 1

    def get_score(self):
        return self.score


    




