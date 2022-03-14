class Banker():

    def __init__(self, balance=0, shelved=0):
        self.balance = balance
        self.shelved = shelved

    def shelf(self, points = 0):
        self.shelved += points
        return self.shelved

    def bank(self):
        pass
        
    def clear_shelf(self):
        self.shelved = 0
        return self.shelved

#Hello