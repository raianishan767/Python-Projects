

class bankAccount:
    
    def __init__(self,owner,amount=0):
        self.owner=owner
        self.amount=amount
    
    def deposit(self):
        amount=int(input("Enter your deposited amount : "))
        if amount>0:
            self.amount+=amount
            print(f"Deposited {amount}tk")
        else:
            print("Invalid deposit")
        print("\n")

    def withdraw(self):
        amount=int(input("Enter your withdrawn amount : "))
        if amount>0 and amount<self.amount:
            self.amount-=amount
            print(f"Withdrawn {amount}tk")
        else:
            print(f"Your remaining balance is : {self.amount}")
            print("And your withdrawn is out of limit. Thank you")
        print("\n")
    
    def viewAcc(self):
        print(f"Name : {self.owner}")
        print(f"Your current balance is : {self.amount}tk")
        print("\n") 

    def start(self):
     
     while True:
        
        print("1.View Account Details")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        option=int(input("Choose (1-4) : "))
        
        if option==1:
             self.viewAcc()
        elif option==2:
             self.deposit()
        elif option==3:
             self.withdraw()
        elif option==4:
            break
        else:
            print("Invalid option.Try again.")
    

m=bankAccount("Sojol")
m.start()
        
