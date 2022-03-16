

    def bank_first_for_two_rounds(self, roller= None, bank=0, shelf = ):
        print('Welcome to Game of Greed')
        wanna_play = input('Wanna play? ')
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
            decision = input("Enter dice to keep (no spaces), or (q)uit: ")
            if decision != 'q':
                print(f"You have {shelf} unbanked points and 2 dice remaining")
                decision2 = input('(r)oll again, (b)ank your points or (q)uit ')
                if decision2 == 'b':
                    print(f'You banked {bank} points in round 2')
                elif decision2 == 'r':
                    print(f"Total score is {bank} points")
                    print("Starting round 3")
                    print("Rolling 6 dice...")
                    rolled_dice = self.roller(6)
                    nums = []
                    for i in rolled_dice:
                        nums.append(str(i))
                    print(','.join(nums))
                    decision3 = input("Enter dice to keep (no spaces), or (q)uit: ")
                    if decision3 == 'q':
                        print(f"You have {shelf} unbanked points and 1 dice remaining")
                        decision4 = input('(r)oll again, (b)ank your points or (q)uit b')
                        if decision4 == 'r':
                            print(f'You banked {shelf} points in round 2')
                            print(f"Total score is {bank} points")
                            print(f'Thanks for playing. You earned {shelf} points')

                for i in rolled_dice:
                    nums.append(str(i))

                print(','.join(nums))
                decision2 = input("Enter dice to keep (no spaces), or (q)uit: ")
                if decision2=="q":
                    print("Total score is 50 points")
                    print("Thanks for playing. You earned 50 points")
    


