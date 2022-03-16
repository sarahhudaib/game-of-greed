from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from collections import Counter

class Game:
    def __init__(self, roller = None):
        self.roller = roller
        self.banker=Banker()
        self.game_logic=GameLogic()
        # python -m game_of_greed.game
        
    @staticmethod
    def quit(score):
        print(f"Total score is {score} points")
        print(f"Thanks for playing. You earned {score} points")
        
        
    def play(self):
        round=0
        unbanked=0
        rolled=0
        remaining = 6
        score = 0
        print("Welcome to Game of Greed")
        wanna_play = input("Wanna play? ")
        if wanna_play == "n":
            print("OK. Maybe another time")
        elif wanna_play =="y":
            print(f"Starting round {round+1}")
            while True:
                round=round+1
                print("Rolling 6 dice...")
                rolled_dice = self.roller(6)
                nums = []
                for i in rolled_dice:
                    nums.append(str(i))
                print(','.join(nums))
                decision = input("Enter dice to keep (no spaces), or (q)uit: ")
                if decision == "q" and round <= 1:
                    print(f"Thanks for playing. You earned {score} points")
                    break
                elif decision != 'q' and decision != 'b'and decision != 'r':
                    user_input = [int(i) for i in decision]
                    remaining -= len(user_input)
                    unbanked = GameLogic().calculate_score(tuple(user_input)) 
                    if rolled!=0 :
                        unbanked +=rolled
                        rolled=0
                    print(f"You have {unbanked} unbanked points and {remaining} dice remaining")
                    decision2 = input('(r)oll again, (b)ank your points or (q)uit ')
                    if decision2 == 'q' and round > 1:
                        Game.quit(score)
                        break
                    elif decision2 == 'b':
                        score += unbanked
                        print(f'You banked {unbanked} points in round {round-1}')
                        print(f'Total score is {score} points')
                        print(f"Starting round {round}")

                    # elif decision2 == 'r':
                        # continue
                    elif decision2 == 'r' and unbanked == 1500:
                        rolled += unbanked
                        remaining =6
                    elif decision2 == 'r':
                        rolled += unbanked
                        remaining =0
                        print(f"Starting round {round}")
                    
                
            
if __name__ == "__main__":
    game = Game( GameLogic.roll_dice )
    game.play()