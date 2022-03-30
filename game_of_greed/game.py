from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from collections import Counter

# python -m game_of_greed.game

class Game:
    def __init__(self, roller = GameLogic.roll_dice):
        self.roller = roller
        self.banker=Banker()
        self.game_logic=GameLogic()
        self.total_score = 0
        self.round = 1
     

    def quit(self, total_score,cheater) :
        if cheater:
            # print(f'Total score is {score} points')
            print(f'Thanks for playing. You earned {total_score} points')
        elif total_score == 0:
            print(f"Thanks for playing. You earned 0 points")
        else:
            # print(f"Total score is {score} points")
            print(f"Thanks for playing. You earned {total_score} points")
    

    def validation(decision, rolled_dice):
        decision_list = [int(i) for i in decision]
        ctr_decision = list(Counter(decision_list).items())
        ctr_rolled_dice = list(Counter(rolled_dice).items())
        keys_rolled_dic = list(Counter(rolled_dice).keys())
        for i in ctr_decision:
            for j in ctr_rolled_dice:
                if i[0] not in keys_rolled_dic:
                    return True
                if i[0] == j[0]:
                    if i[1] > j[1]:
                        return True
        return False


    def print_decision(self, rolled_dice):
        nums = []
        for i in rolled_dice:
            nums.append(str(i))
        print('*** '+','.join(nums))
        
        
    def play(self):
        # print("Welcome to Game of Greed")
        print('(y)es to play or (n)o to decline')
        wanna_play = input()
        if wanna_play == "n":
            print("OK. Maybe another time")
        elif wanna_play =="y":
            # total_score=0
            # round=1
            unbanked=0
            rolled=0
            remaining = 6
            play=True
            zilch = False
            cheater = False
            # print(f"Starting round {round}")
           
            while play:
                if self.total_score > 10000 or self.round > 6:
                    self.quit(self.total_score, cheater)
                    play=False

                # print(f"Rolling {remaining} dice...")
                rolled_dice = self.roller(remaining)
                self.print_decision(rolled_dice)

                if GameLogic().calculate_score(rolled_dice) == 0:
                    zilch = True
                    print('Zilch!!! Round over')
                    print(f'You banked 0 points in round {self.round}')
                    # print(f'Total score is {score} points')
                    self.round+=1
                    # print(f"Starting round {round}")
                    remaining = 6
                    continue
                
                print("Enter dice to keep, or (q)uit:")
                decision = input()
                
                if decision== "q":
                    rolled=0
                    if zilch:
                        # print('Total score is 0 points')
                        print('Thanks for playing. You earned 0 points')
                        break
                    self.quit(self.total_score,cheater)
                    play=False
                    
                elif decision != 'q' and decision != 'b'and decision != 'r':
                    if Game.validation(decision, rolled_dice):
                        cheater = True
                        print('Cheater!!! Or possibly made a typo...')
                        # Game.print_decision(rolled_dice)
                        print('Enter dice to keep, or (q)uit:')
                        decision = input()
                        
                    user_input = [int(i) for i in decision]
                    remaining -= len(user_input)

                    int_user_input = []
                    x = tuple(user_input)
                    for i in x:
                        int_user_input.append(int(i))
                    unbanked = self.game_logic.calculate_score(int_user_input) 

                    if rolled!=0 :
                      unbanked +=rolled   
                    rolled=0
                    print(f"You have {unbanked} unbanked points and {remaining} dice remaining")

                    print("(r)oll again, (b)ank your points or (q)uit:")
                    decision2 = input()
                    if decision2 == 'q':
                        self.quit(self.total_score,cheater)
                        rolled=0
                        play=False
                    
                    elif decision2 == 'b':
                        self.total_score += unbanked
                        print(f'You banked {unbanked} points in round {self.round}')
                        # print(f'Total score is {score} points')
                        self.round+=1
                        rolled=0
                        remaining =6
                        # print(f'Starting round {round}')
                    
                    elif decision2 == 'r' and unbanked == 1500:
                        rolled += unbanked
                        remaining =6
                    elif decision2 == 'r':
                        rolled += unbanked
                        if remaining==0:
                            self.total_score += unbanked
                            remaining =6
                            # print(f'Starting round {round}')


                    
                
            
if __name__ == "__main__":
    game = Game( GameLogic.roll_dice )
    game.play()





    