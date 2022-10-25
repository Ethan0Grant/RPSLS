import random
from Player import Player

class AI(Player):
    def __init__(self):
        super().__init__()

    def give_gesture(self):
        self.move = random.choice(self.gesture)
        print("{} played {}".format(self.name, self.move))


    def set_name(self): 
        self.name = "AI_Jeff" 