"""
TODO:
* generate account number
* connect user/admin menu interactions
* add more privacy, especially on Bank class
"""

import datetime

class Bank:
    Bank_Balance = 0
    Loan_Given = 0
    Can_Loan = True
    users = {}

class User(Bank):
    def __init__(self, acNumber, name, address, email, acType):
        self.__acNumber = acNumber
        self.__name = name
        self.__address = address
        self.__email = email
        self.__acType = acType
        self.__balance = 0
        self.__loaned_time = 0
        self.__loaned_amount = 0
        self.__transactions = []

    @property
    def Balance(self):
        print(f"Your Current Balance: {self.__balance}")

    def Deposit(self, amount):
        amount = self.pay_loan(amount)
        if(amount > 0):
            self.__balance += amount
            super().Bank_Balance += amount
            print(f"{amount}/- Diposited Successfully!")
            self.Balance
            self.transaction('+', amount, 'Deposited')

    def Withdraw(self, amount):
        if(super().Bank_Balance < amount):
            print("Oops! We are bankrupt")
        elif(self.__balance >= amount):
            self.__balance -= amount
            super().Bank_Balance -= amount
            print(f"{amount}/- Withdrawn Successfully!")
            self.Balance
            self.transaction('-', amount, 'Withdrawn')
        else:
            print("Withdrawal amount exceeded")
            self.Balance

    def take_loan(self, amount):
        if(super().Can_Loan is True) and (super().Bank_Balance > 0):
            if(self.__loaned_time < 2):
                while(super().Bank_Balance < amount):
                    print(f"Sorry, current laon limit is {super().Bank_Balance}")
                    amount = int(input("New Loan Amount: "))
                    if(amount < 1):
                        print("Loan Request is Cancelled")
                        return
                self.Deposit(amount)
                self.__loaned_time += 1
                self.__loaned_amount += amount
                super().Loan_Given += amount
                super().Bank_Balance -= amount
                self.transaction('+', amount, 'Took Loan')
            else:
                print("Denied! You've already taken max number of loans")
        else:
            print("Sorry, This bank is not offering Loans at this moment!")

    def pay_loan(self, amount) -> int:
        if(self.__loaned_amount>0):
            will_pay = ''
            while((will_pay != 'Y') and (will_pay != 'N')):
                will_pay = input("Would you like to payback your loans (Y/N)? --")
                if((will_pay != 'Y') and (will_pay != 'N')):
                    print("Invalid entry! Enter Y or N please")
            if(will_pay == 'Y'):
                # check if amount > loan
                self.__loaned_amount -= amount
                super().Bank_Balance += amount
                super().Loan_Given -= amount
                print(f"Loan paid successfully! Now you have {self.__loaned_amount}/- loan left")
                self.transaction('', amount, 'Paid Loan')
                # return extra
        return amount


    def transfer(self, acNumber, amount):
        reciever = super().users[acNumber][0]
        reciever.Deposit(amount)
        print(f"Successfully transfered {amount}/- to AC:{acNumber}")
        self.Balance
        self.transaction('-', amount, 'Transfered')

    def transaction(self, change, amount, note):
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.__transactions.append((time, change, amount, note))

    def check_history(self):
        counter = 1
        for Tn in self.__transactions:
            print(f"{counter}. {Tn[0]} [{Tn[3]}] {Tn[1]}{Tn[2]}/-")
            counter += 1


class Admin(Bank):
    def __init__(self, acNumber, name, address, email):
        self.__acNumber = acNumber
        self.__name = name
        self.__address = address
        self.__email = email

    def show_all_users(self):
        for user in super().users:
            if(user[2]=='user'):
                ins = user[0]
                print("---------------------------")
                print("Account Number  :", ins.__acNumber)
                print("User Name       :", ins.__name)
                print("User E-Mail     :", ins.__email)
                print("User Address    :", ins.__address)
                print("Account Type    :", ins.__acType)
                print("Current Balance :", ins.__balance)
                print("Loan Recieved   :", ins.__loaned_time)

    def delete_user(self, acNumber):
        if super().users[acNumber][2] == 'admin':
            print("Error! Can't delete another Admin account")
        else:
            del super().users[acNumber]
            print(f"Account no. {acNumber} is Deleted successfully")

    @property
    def check_balance():
        print("Current Bank Balance:", super().Bank_Balance)

    @property
    def check__loaned_time():
        print("Total Loans Given:", super().Loan_Given)

    @property
    def toggle_loan():
        super().Can_Loan = not super().Can_Loan
        

def generateAC():
    pass

print("---------------------------")
print("Welcome to Terminal Banking")

op = Bank()
cmd = '0'
secret_key = '********'

while(True):
    caller = None
    signed = None
    print("---------------------------")
    print("What would you like to do ?")
    print("[1] Create an Account")
    print("[2] Login to your Account")
    print("[3] Exit")
    print("---------------------------")
    cmd = input("ENTRY: ")
    print("---------------------------")
    if(cmd=='3'):
        print("Thanks for visiting Terminal Banking, Come again\n")
        break
    if(cmd=='1' or cmd=='2'):
        while(signed is None):
            ac = input("Access Type (USER or ADMIN): ").lower()
            if(ac=='user' or ac=='admin'): signed = ac
            else:
                print("Invalid entry! Try again")
        if(signed == 'admin'):
            access_key = input("Enter Admin Access Key: ")
            if(access_key != secret_key):
                print("Access Denied! Invalid Key")
                continue

    if(cmd=='1'):
        name = input("Enter you Name: ")
        address = input("Enter your Address: ")
        email = input("Enter a valid E-mail: ")
        acType = None
        while(signed is 'user'):
            acType = input("Account Type (Savings/Current): ").lower()
            if(acType!='savings' and acType!='current'):
                print("Invalid account type. Enter Savings or Current")
            else: break
        
        acNumber = generateAC()

        if(signed is 'admin'):
            caller = Admin(acNumber, name, address, email)
        else:
            caller = User(acNumber, name, address, email, acType)

        password = input("Enter new Password: ")
        op.users[acNumber] = (caller, password, signed)
        print("Account created Successfully!")
        print("Signed in to AC:", acNumber)
        print("---------------------------")

    elif(cmd=='2'):
        print("Enter Valid Login Info -")
        acNumber = input("Account Number: ")
        password = input("Password: ")
        if (acNumber not in op.users) or (password != op.users[acNumber][1]):
            print("Invalid AC number or password! Please try again.")
        else:
            print("Signed in to AC:", acNumber)
            caller = op.users[acNumber][0]
        
    else:
        print("Invalid Entry! Try Entering 1-3\n")
        continue

    while(signed == 'user'):
        print("---------------------------")
        print("What would you like to do ?")
        print("[1] Check Balance")
        print("[2] Withdraw Amount")
        print("[3] Deposit Amount")
        print("[4] Transfer Amount")
        print("[5] Apply for Loan")
        print("[6] Check Transaction History")
        print("[0] Logout from Account")
        print("---------------------------")
        c = input("ENTRY: ")
        print("---------------------------")

        if c == '1':
            pass
        elif c == '2':
            pass
        elif c == '3':
            pass
        elif c == '4':
            pass
        elif c == '5':
            pass
        elif c == '6':
            pass
        elif c == '0':
            print("Logout Successful")
            signed = 'none'
        else:
            print("Invalid Entry! Try entering 0-6")

    while(signed == 'admin'):
        print("---------------------------")
        print("What would you like to do ?")
        print("[1] Check All Users")
        print("[3] Delete a User account")
        print("[2] Check Total Bank Balance")
        print("[4] Check Loan amount")
        print("[5] Toggle loan feature")
        print("[0] Logout from Account")
        print("---------------------------")
        c = input("ENTRY: ")
        print("---------------------------")

        if c == '1':
            pass
        elif c == '2':
            pass
        elif c == '3':
            pass
        elif c == '4':
            pass
        elif c == '5':
            pass
        elif c == '0':
            print("Logout Successful")
            signed = 'none'
        else:
            print("Invalid Entry! Try entering 0-5")
        