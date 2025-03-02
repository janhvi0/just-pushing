# class dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def barking(self):
#         print(f'{self.name} barks very much')

# dog1 = dog("goldy", 2)
# dog2= dog("sheru",4)
# print(dog1)
# print(dog1.name)
# print(dog1.age)
# print(dog.barking(dog1))
# print(dog.barking(dog2))


class Banking:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance

    def deposite(self,amount):
        self.balance+=amount
        print(f'{amount} is deposited. Current balance {self.balance}')

    def withdrawal(self,amount):
        if amount>self.balance:
            print(f"you dont't have enough balance. Current balance is {self.balance}")
            
        else:
            self.balance-=amount
            print(f'{amount} withdrawn. Current balance {self.balance}')

    def get_balance(self):
        return self.balance
    

acc1 = Banking("Janhvi", 1000)
print(acc1.owner)
print(acc1.balance)
acc1.deposite(300)
acc1.withdrawal(400)
acc1.withdrawal(1000)
print(acc1.get_balance())




