class Game:
    def __init__(self, roller = None):
        self.roller = roller

    def play(self):
        print("Welcome to Game of Greed")
        wanna_play = input("Wanna play? ")
        if wanna_play == "n":
            print("OK. Maybe another time")
        else:
            print("Starting round 1")
            print("Rolling 6 dice...")
            rolled_dice = self.roller(6)
            nums = []
            for i in rolled_dice:
                nums.append(str(i))
            print(','.join(nums))
            # print(*rolled_dice, sep=',')
            decision = input("Enter dice to keep (no spaces), or (q)uit: ")
            if decision=="q":
                print("Thanks for playing. You earned 0 points")
            #ahmad code form here 
            elif decision == "5":
                print("You have 50 unbanked points and 5 dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit b")
                print("You banked 50 points in round 1")       
                print("Total score is 50 points")       
                print("Starting round 2")        
                print("Rolling 6 dice..." )      
                        
                        
                rolled_dice = self.roller(6)
                nums = []
            
                for i in rolled_dice:
                    nums.append(str(i))

                print(','.join(nums))
                decision2 = input("Enter dice to keep (no spaces), or (q)uit: ")
                if decision2=="q":
                    print("Total score is 50 points")
                    print("Thanks for playing. You earned 50 points")
    


if __name__ == "__main__":
    from game_logic import GameLogic
    game = Game(GameLogic.roll_dice)
    game.play()