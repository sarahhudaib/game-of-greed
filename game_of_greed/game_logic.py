from collections import Counter
from random import randint
from typing import Tuple

class GameLogic:
    @staticmethod
    def roll_dice(num):
        #your code go here 
        #output tuple with ranom value between i and 6

        roll_dice_data=[]

        for i in range(num):
            roll_dice_data+=[randint(1, 6)]

        return tuple(roll_dice_data)

        
       

  
    @staticmethod
    def calculate_score(dice):
        pass

if __name__=="__main__":
    # len= 6
    tuple_data=[]
    for i in range(5):
        tuple_data+=[randint(1, 6)]
    print(tuple(tuple_data))





