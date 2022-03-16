from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from collections import Counter

class Game:
    def __init__(self, roller = None):
        self.roller = roller
        self.banker=Banker()
        self.game_logic=GameLogic()
        # self.points=points
        # python -m game_of_greed.game
        

    def quit(score):
        print(f"Total score is {score} points")
        print(f"Thanks for playing. You earned {score} points")
        
        
    def play(self):
        round=0
        unbanked=0
        rolled=0
        print("Welcome to Game of Greed")
        wanna_play = input("Wanna play? ")
        if wanna_play == "n":
            print("OK. Maybe another time")
        elif wanna_play =="y":
            while True:
                round=round+1
                print(f"Starting round {round}")
                print("Rolling 6 dice...")
                rolled_dice = self.roller(6)
                nums = []
                for i in rolled_dice:
                    nums.append(str(i))
                print(','.join(nums))
                decision = input("Enter dice to keep (no spaces), or (q)uit: ")
                if decision== "q":
                    print("Thanks for playing. You earned 0 points")
                    break
                else :
         
                    remaining= 6-len(decision)
                    str_tuple = tuple(decision)
                    int_list=[]
                    for i in str_tuple:
                        int_list.append(int(str_tuple[i]))
                    int_tuple = tuple(int_list)
                    score = Banker.shelf(GameLogic.calculate_score(int_tuple))
                    # print(f"You have {score} unbanked points and {remaining} dice remaining")
                    
                    # if decision != 'q' and decision != 'b'and decision != 'r':
                    #     user_input = [int(i) for i in decision]
                    #     print(tuple(decision))
                    #     unbanked= self.banker.shelf(GameLogic.calculate_score(tuple(decision)))
                    #     if rolled!=0 :
                    #             unbanked +=rolled
                    #             rolled=0
                    # remaining= 6-len(decision)
                    print(f"You have {score} unbanked points and {remaining} dice remaining")
                    decision2 = input('(r)oll again, (b)ank your points or (q)uit ')
                    if decision2 == 'q':
                        Game.quit(self.banker.bank)
                        break
                    elif decision2 == 'b':
                        print(f'You banked {self.banker.bank} points in round {round}')
                    elif decision2 == 'r':
                        print(f"Total score is {self.banker.bank} points")
                    
                
            
if __name__ == "__main__":
    game = Game( GameLogic.roll_dice )
    game.play()