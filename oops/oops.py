# class bank():
#     def __init__(self):
#         self.id=int(input("Enter Id : "))
#         self.name=input("Enter Your Name :")
#         self.balance=0
#     def avail_bal(self):
#         print("Available Balance :",self.balance)
#     def deposit(self):
#         deposit_amt=int(input("Enter Deposit Amount :"))
#         self.balance+=deposit_amt
        
        
# customer1=bank()
# customer1.deposit()
# customer1.avail_bal()

class bank():
    def __init__(self,id,name,balance):
        self.id=id
        self.name=name
        self.balance=balance
    def avail_bal(self):
        print("Available Balance :",self.balance)
    def deposit(self,amt):
        self.balance+=amt
        
        
customer1=bank(100,'Akhil',0)
customer1.deposit(100000)
customer1.avail_bal()


