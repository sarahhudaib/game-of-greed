from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game:
    def __init__(self, roller = None):
        self.roller = roller
        self.banker=Banker()
        self.game_logic=GameLogic()

    def quit(score):
        """a function that will be called when we want to quit or finish the game"""
        if score ==0:
            print(f"Thanks for playing. You earned {score} points")
        else:   
            print(f"Total score is {score} points")
            print(f"Thanks for playing. You earned {score} points")
        
        
    def play(self):
        """this func will make the game  go through the test files"""
        print("Welcome to Game of Greed")
        wanna_play = input("Wanna play? ")
        if wanna_play == "n":
            print("OK. Maybe another time")
        elif wanna_play =="y":
            score=0
            round=1
            unbanked=0
            rolled=0
            remaining = 6
            play=True
            print(f"Starting round {round}")
           
            while play:
                print("Rolling 6 dice...")
                rolled_dice = self.roller(6)
                nums = []
                for i in rolled_dice:
                    nums.append(str(i))
                print(','.join(nums))
                decision = input("Enter dice to keep (no spaces), or (q)uit: ")
                if decision== "q":
                    Game.quit(score)
                    rolled=0
                    play=False
                elif decision != 'q' and decision != 'b'and decision != 'r':
                    user_input = [int(i) for i in decision]
                    remaining -= len(user_input)
                    unbanked = GameLogic().calculate_score(tuple(user_input)) 
                    if rolled!=0 :
                      unbanked +=rolled   
                    rolled=0
                    print(f"You have {unbanked} unbanked points and {remaining} dice remaining")
                    decision2 = input('(r)oll again, (b)ank your points or (q)uit ')
                    if decision2 == 'q':
                        Game.quit(score)
                        rolled=0
                        play=False
                    
                    elif decision2 == 'b':
                        score+=unbanked
                        print(f'You banked {unbanked} points in round {round}')
                        print(f'Total score is {score} points')
                        round+=1
                        rolled=0
                        remaining =6
                        print(f'Starting round {round}')
                    
                    elif decision2 == 'r' and unbanked == 1500:
                        rolled += unbanked
                        remaining =6
                    elif decision2 == 'r':
                        rolled += unbanked
                        if remaining==0:
                            score+=unbanked
                            remaining =6
                            print(f'Starting round {round}')
                             
if __name__ == "__main__":
    game = Game( GameLogic.roll_dice )
    game.play()