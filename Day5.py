class Bankaccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError ("Insufficient Balance")
        self.balance -= amount

    def __eq__(self, other):
        if isinstance(other,Bankaccount):
            return self.owner == other.owner and self.balance == other.balance
        return False
    
    def __add__(self, other):
        new_owner = self.owner + other.owner
        total = self.balance + other.balance
        return Bankaccount(new_owner,total)
    
    def __repr__(self):
        return f"{self.owner}'s balance is {self.balance}"
    
acc1 = Bankaccount("Aryan", 1000)
acc2 = Bankaccount("Aryan", 1000)
acc3 = Bankaccount("Aryan", 500)

acc1_repr = repr(acc1)
print(acc1_repr)

print(acc1 == acc2)

joint_acc1_acc2 = acc1 + acc2
print(joint_acc1_acc2)