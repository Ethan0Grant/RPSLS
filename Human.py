from Player import Player


class Human(Player):
    def __init__(self):
        super().__init__()
    
    def give_gesture(self):
        while True:
            print()
            gesture = input("Please input a number correspoinding to the gesture: ")
            if gesture in ['0', '1', '2', '3', '4']: 
                self.move = self.gesture[int(gesture)]
                print("{} played {}.".format(self.name, self.move))
                break
            else:
                print ("Invalid entry.")


    def set_name(self):
        print()
        self.name = input("Please input player name: ")
