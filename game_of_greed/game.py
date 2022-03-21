from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from collections import Counter

class Game:
    def __init__(self, roller = None):
        self.roller = roller
        self.banker=Banker()
        self.game_logic=GameLogic()
        # python -m game_of_greed.game
        

    def quit(score) :
        if score == 0:
            print(f"Thanks for playing. You earned 0 points")
        else:
            print(f"Total score is {score} points")
            print(f"Thanks for playing. You earned {score} points")
    
    # def validation(decision, rolled_dice):
        # # method 1
        # decision_list = [int(i) for i in decision]
        # result = set(rolled_dice).issubset(decision_list)
        # if GameLogic.calculate_score(rolled_dice) < GameLogic.calculate_score(tuple(decision_list)):
        #     validation = False
        # else:
        #     validation = True
        # return result and validation

        # # method 2
        # decision_list = [int(i) for i in decision]
        # rolled_list = list(rolled_dice)
        # result = set(decision_list).issubset(rolled_list)

        # # method 3
        # ctr_decision = Counter(decision)
        # ctr_rolled_dice = Counter(rolled_dice)
        


    def print_decision(rolled_dice):
        nums = []
        for i in rolled_dice:
            nums.append(str(i))
        print(','.join(nums))
        
        
    def play(self):
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
            zilch = False
            print(f"Starting round {round}")
           
            while play:
                print(f"Rolling {remaining} dice...")
                rolled_dice = self.roller(remaining)
                # nums = []
                # for i in rolled_dice:
                #     nums.append(str(i))
                # print(','.join(nums))
                Game.print_decision(rolled_dice)

                if GameLogic().calculate_score(rolled_dice) == 0:
                    zilch = True
                    print('Zilch!!! Round over')
                    print(f'You banked 0 points in round {round}')
                    print(f'Total score is {score} points')
                    round+=1
                    print(f"Starting round {round}")
                    remaining = 6
                    continue
                decision = input("Enter dice to keep (no spaces), or (q)uit: ")

                # if Game.validation(decision, rolled_dice):
                #     print('Cheater!!! Or possibly made a typo...')
                #     Game.print_decision(rolled_dice)
                #     decision = input("Enter dice to keep (no spaces), or (q)uit: ")
                
                if decision== "q":
                    rolled=0
                    if zilch:
                        print('Total score is 0 points')
                        print('Thanks for playing. You earned 0 points')
                        break
                    Game.quit(score)
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


