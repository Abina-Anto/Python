class Bank:
    def __init__(self):
        self.balance = 0
        print("__Create an Account__")
        self.name = input("Enter the name:")
        self.acctno = int(input("Enter the account number:"))
        self.typeofac = input("Enter the type of account:")

    def deposit(self):
        amount = int(input("Enter the amount to be deposited:"))
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self):
        amount = int(input("Enter the amount to be withdrawn:"))
        if self.balance >= amount:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display(self):
        print("Name:", self.name)
        print("Account Number:", self.acctno)
        print("Type of Account:", self.typeofac)
        print("Balance:", self.balance)

a = Bank()

while True:
    print("\n1.Deposit\n2.Withdrawal\n3.Balance\n4.Exit\n")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        a.deposit()
    elif ch == 2:
        a.withdraw()
    elif ch == 3:
        a.display()
    elif ch == 4:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Wrong Choice!")
