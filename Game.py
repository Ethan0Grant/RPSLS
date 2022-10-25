from Player import Player
from Human import Human
from AI import AI
from time import sleep


class Game:
    def __init__(self):
        self.welcome()
        self.winner_name = None
        self.round_winner_name = None
        self.player_count = self.get_player_count() 
        self.rules = {'rock':['scissors', 'lizard'], 'scissors':['paper', 'lizard'], 'paper':['rock', 'spock'], 'lizard':['spock', 'paper'], 'spock':['scissors', 'rock']}
        self.game_types = {1: [Human(),AI()], 2:[Human(), Human()], 3:[AI(), AI()]}
        self.p1, self.p2 = self.create_players()

    def welcome(self):
        print('Welcome to RPSLS!!')
        # sleep(1)
        print('Each player picks a gesture and reveals it at the same time. The winner is the one who gets 2 wins. In a tie, the process is repeated until a winner is found.')
        # sleep(1)
        print('1You can choose between Rock, Paper, Scissors, Lizard or Spock')
        # sleep(1)
        print('Rock crushes Scissors')
        # sleep(1)
        print('Scissors cuts Paper')
        # sleep(1)
        print('Paper covers Rock')
        # sleep(1)
        print('Rock crushes Lizard')
        # sleep(1)
        print('Lizard poisons Spock')
        # sleep(1)
        print('Spock smashes Scissors')
        # sleep(1)
        print('Scissors decapitates Lizard')
        # sleep(1)
        print('Lizard eats Paper')
        # sleep(1)
        print('Paper disproves Spock')
        # sleep(1)
        print('Spock vaporizes Rock')
        # sleep(1)
        

    def prompt_instruction(self):
        print('Rock(0)\nPaper(1)\nScissors(2)\nLizzard(3)\nSpock(4)')



    def get_player_count(self):
            type = input("Please input player count: (Min:1 Max:3): ")
            if type in ['1', '2', '3']:
                return int(type)
            else:
                print("Invalid input.")  


    def check_move(self):
        if self.p1.move in self.rules[self.p2.move]:
            self.p2.point()
            self.round_winner_name = self.p2.name
       
        elif self.p2.move in self.rules[self.p1.move]:
            self.p1.point()
            self.round_winner_name = self.p1.name

        else:
            print("Tie.")


    def create_players(self):
        return self.game_types[self.player_count]

    
    def play_round(self):
        self.p1.give_gesture()
        self.p2.give_gesture()
        self.check_move()
        print("{} won the round!".format(self.round_winner_name))

    
    def tell_winner(self):
        print("{} won the game!".format(self.round_winner_name))

    
    def get_winner(self):
        if self.p2.get_score() == 2:
            self.winner_name = self.p1.name
        
        else:
            self.winner_name = self.p2.name
    
   
    def play_game(self):
        while True:
            self.p1.set_name()
            self.p2.set_name()
            if self.player_count == 3:
                self.p2.name = "AI_Bob"
                
            while self.p1.get_score() < 2 and self.p2.get_score() < 2:
                self.prompt_instruction()
                sleep(1)
                self.play_round()
                sleep(1)
            self.get_winner()
            self.tell_winner()
            sleep(3)
            
            if input("Would you like to play again? (Y/N) ") != "y":
                break 

            self.__init__()


        print("Thanks for playing!")
            
            
