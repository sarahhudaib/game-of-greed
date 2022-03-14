from collections import Counter
from random import randint
from typing import Tuple

class GameLogic:
    
    @staticmethod
    def roll_dice(num):
        #output tuple with random value between i and 6

        roll_dice_data=[]

        for i in range(num):
            roll_dice_data+=[randint(1, 6)]

        return tuple(roll_dice_data)


    @staticmethod
    def calculate_score(dice_results):
        ctr = Counter(dice_results)
        ctr = list(ctr.items())
        ctr.sort(key=lambda x: (-x[1], x[0]))
        print(ctr)
        score = 0
        count = 0
        if ctr == [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)] :
            score = 1500
        else: 
            for i in ctr: 
                print(i[0])
                if i[1] == 3 and i[0] != 1:
                    score += i[0] * 100
                if i[1] == 4:
                    score += 400  
                if i[1] == 5:
                    score += 600
                if i[1] == 6 and i[0] == 1:
                    score += 4000
                elif  i[1] == 6:
                    score += 800
                if i[0] == 1 and i[1] < 4:
                    if i == (1, 3):
                        score += 1000
                    else:
                        score += i[1]*100
                        if i[1] == 2:
                            count +=1
                if i[0] == 5 and i[1] < 3:
                    score += i[1]*50
                    if i[1] == 2:
                        count +=1
                elif i[1] == 2:
                    count += 1
                if count == 3:
                    score += 1500
        return score








