class BankAccount :
    def __init__(self,account_number,owner_name,balance):
        self.account_number = account_number
        self.ower_name = owner_name
        self.balance = balance
   
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"current new_balance ={self.balance}")
    def withdraw(self,withdraw_amount):
        self.balance = self.balance - withdraw_amount
        print(f"Take the amount!!! remaining balance:{self.balance}")
    def checkbalance(self):
        print(f"Your currnt balance is : {self.balance}")
    
        
acc1 = BankAccount(1001,"jai",80_000)

acc1.deposit(100)
acc1.withdraw(50)
acc1.checkbalance()



