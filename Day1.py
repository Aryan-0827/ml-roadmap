class Bankaccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
    
    def __str__(self):
        return f"{self.owner}'s balance is {self.balance}"
    

acc = Bankaccount("Aryan", 5000)
acc.deposit(1000)
print(acc)

acc.withdraw(200)
print(acc.balance)