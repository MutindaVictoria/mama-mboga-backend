class Payment:
    def__init__(self,name,phone_number,account_balance):
        self.name = name
        self.phone_number = phone_number
        self.account_balance = account_balance
    
    def check_balance(self):
        print(f"Your Account balance is{self.account_balance}")
    def pay_now(self,total):
        if total>self.account_balance:
            print(f" You have insufficient funds  in your account balance to pay{tota}your account balance is:{self.account_balance}")
        else:
            self.account_balance-= total  
            print(f"You paid {total},your new account balance is {self.account_balance}")
