      class Bank:

          def __init__(self, bal):
              self.balance = bal

    def deposit(self):
        amount = float(input("Enter Deposit Amount: "))
        self.balance = self.balance + amount
        print("Deposited")

    def withdraw(self):
        amount = float(input("Enter Withdraw Amount: "))

        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdraw Successful")
        else:
            print("No Balance")

    def check(self):
        print("Balance:", self.balance)

    def receipt(self, name, acc):

        print("\n------ BANK RECEIPT ------")
        print("Name       :", name)
        print("Account No :", acc)
        print("Final Bal  :", self.balance)
        print("Status     : Completed")
        print("--------------------------")



name = input("Enter Name: ")
acc = input("Enter Account No: ")

b = float(input("Enter Current Balance: "))

obj = Bank(b)

print("\n1 Deposit")
print("2 Withdraw")
print("3 Check Balance")

ch = int(input("Enter Choice: "))

if ch == 1:
    obj.deposit()

elif ch == 2:
    obj.withdraw()

elif ch == 3:
    obj.check()

else:
    print("Wrong Choice")

obj.receipt(name, acc)