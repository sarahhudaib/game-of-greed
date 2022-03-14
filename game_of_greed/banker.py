class Banker():
    """Handle banking points"""

    def __init__(self, balance=0, shelved=0):
        self.balance = balance
        self.shelved = shelved

    def shelf(self, points = 0):
        """function temporarily store unbanked points"""
        self.shelved += points
        return self.shelved

    def bank(self):
        """Function add any points on the shelf to total and reset shelf to 0"""
        self.balance += self.shelved
        self.clear_shelf()

    def clear_shelf(self):
        """clear_shelf should remove all unbanked points"""
        self.shelved = 0
        return self.shelved
    
if __name__ == "__main__":
    banker = Banker()
    banker.shelf(100)
    print(banker.shelved)
    
    banker = Banker()
    banker.shelf(200)
    banker.bank()
    print(banker.shelved)
    
    banker = Banker()
    banker.shelf(200)
    banker.bank()
    print(banker.shelved == 0)
    banker.shelf(50)
    banker.clear_shelf()
    print(banker.balance == 100)



