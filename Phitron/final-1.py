from datetime import datetime
import random
valid_chars = "0123456789_abcdefghijklmnopqrstuvwxyz"

class Bank:
    _Bank_Balance = 0
    _Loan_Given = 0
    _Can_Loan = True
    _users = {}

    def generate_account(self, username):
        while(True):
            acNumber = username
            for c in range(5):
                acNumber += random.choice(valid_chars)
            if acNumber not in self._users: return acNumber

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
    def Balance(self) -> int: return self.__balance
    @property
    def Loaned(self) -> int: return self.__loaned_amount
    @property
    def account(self) -> str: return self.__acNumber

    def show_Balance(self):
        print(f"Your Current Balance: {self.__balance}/-")

    def Deposit(self, amount):
        self.__balance += amount
        Bank._Bank_Balance += amount
        self.transaction('+', amount, 'Deposited')
        print(f"{amount}/- Diposited Successfully!")
        self.show_Balance()

    def Withdraw(self, amount):
        if(self.__balance < amount):
            print("Withdrawal amount exceeded")
            self.show_Balance()
        elif(Bank._Bank_Balance < amount):
            print("Oops! We are bankrupt")
            if(Bank._Bank_Balance > 0):
                limit = min(Bank._Bank_Balance, self.__balance)
                print(f"Your current withdrawal limit: {limit}/-")
        else:
            self.__balance -= amount
            Bank._Bank_Balance -= amount
            self.transaction('-', amount, 'Withdrawn')
            print(f"{amount}/- Withdrawn Successfully!")
            self.show_Balance()

    def take_loan(self):
        if(Bank._Can_Loan is True) and (Bank._Bank_Balance > 0):
            if(self.__loaned_time < 2):
                amount = int(input("Enter loan amount: "))
                if(Bank._Bank_Balance < amount):
                    print(f"Sorry, current laon limit is {Bank._Bank_Balance}")
                else:
                    self.Deposit(amount)
                    self.__loaned_time += 1
                    self.__loaned_amount += amount
                    Bank._Loan_Given += amount
                    Bank._Bank_Balance -= amount
                    self.transaction('+', amount, 'Took Loan')
            else:
                print("Denied! You've already taken max number of loans")
        else:
            print("Sorry, This bank is not offering Loans at this moment!")

    def pay_loan(self, amount):
        self.__loaned_amount -= amount
        Bank._Loan_Given -= amount
        Bank._Bank_Balance += amount
        self.transaction('~', amount, 'Paid Loan')
        print("Loan paid successfully!", end = ' ')
        if(self.__loaned_amount != 0): print(f"Now you have {self.__loaned_amount}/- loan left")

    def transfer(self, acNumber, amount):
        reciever = Bank._users[acNumber][0]
        reciever.__balance += amount
        reciever.transaction('+', amount, 'Transfered')
        self.__balance -= amount
        self.transaction('-', amount, 'Transfered')
        print(f"Successfully transfered {amount}/- to AC:{acNumber}")
        self.show_Balance()

    def transaction(self, change, amount, note):
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.__transactions.append((time, change, amount, note))

    def check_history(self):
        if(len(self.__transactions)>0):
            counter = 1
            for Tn in self.__transactions:
                print(f"{counter}. {Tn[0]} [{Tn[3]}] {Tn[1]}{Tn[2]}/-")
                counter += 1
        else: print("You haven't made any Transactions yet!")

    def __repr__(self) -> str:
        rep = f"""
        Access Type     :User
        Account Number  :{self.__acNumber}
        User Name       :{self.__name}
        User E-Mail     :{self.__email}
        User Address    :{self.__address}
        Account Type    :{self.__acType}
        Current Balance :{self.__balance}
        Loan Recieved   :{self.__loaned_time}
        """
        return rep


class Admin(Bank):
    def __init__(self, acNumber, name, address, email):
        self.__acNumber = acNumber
        self.__name = name
        self.__address = address
        self.__email = email

    def show_all__users(self):
        for (key, val) in Bank._users.items():
            print(val[0])

    def delete_user(self, acNumber):
        del Bank._users[acNumber]
        print(f"Account no. {acNumber} is Deleted successfully")

    @property
    def check_balance(self):
        print("Current Bank Balance:", Bank._Bank_Balance)

    @property
    def check_loaned(self):
        print("Total Loans Given:", Bank._Loan_Given)

    @property
    def toggle_loan(self):
        Bank._Can_Loan = not Bank._Can_Loan
        if(Bank._Can_Loan is True): print("Loans Turned ON: _users can take loans now")
        else: print("Loans Turned OFF: _users can't take loans now")

    def __repr__(self) -> str:
        rep = f"""
        Access Type     :Admin
        Account Number  :{self.__acNumber}
        User Name       :{self.__name}
        User E-Mail     :{self.__email}
        User Address    :{self.__address}
        """
        return rep
        

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
        email = ''
        while(True):
            email = input("Enter a valid E-mail: ")
            if ('@' not in email) or ('.' not in email):
                print("Invalid entry! Email must contain '@' and '.'")
            elif len(email.split("@")[0]) < 5:
                print("Invalid entry! Too short")
            elif not all(c in valid_chars+'.@' for c in email):
                print('Invalid character Error! Only use [a-z],[0-9],[@],[.],[_]')
            else:
                print("* Email Varification: Valid *")
                break

        acNumber = Bank().generate_account(email.split("@")[0][:5])

        acType = None
        while(signed == 'user'):
            acType = input("Account Type (Savings/Current): ").lower()
            if(acType!='savings' and acType!='current'):
                print("Invalid account type. Enter Savings or Current")
            else: break

        if(signed == 'admin'):
            caller = Admin(acNumber, name, address, email)
        else:
            caller = User(acNumber, name, address, email, acType)

        password = input("Enter new Password: ")
        Bank()._users[acNumber] = (caller, password, signed)
        print("Account created Successfully!")
        print("Signed in to AC:", acNumber)

    elif(cmd=='2'):
        print("Enter Valid Login Info -")
        acNumber = input("Account Number: ")
        password = input("Password: ")
        if (acNumber not in Bank()._users) or (password != Bank()._users[acNumber][1]):
            print("Invalid AC number or password! Please try again.")
            continue
        else:
            print("Signed in to AC:", acNumber)
            caller = Bank()._users[acNumber][0]
        
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
            caller.show_Balance()

        elif c == '2':
            amount = input("Enter withdrawal Amount: ")
            if amount.isnumeric() and (int(amount) != 0): caller.Withdraw(int(amount))
            else: print("Invalid Entry")

        elif c == '3':
            amount = input("Enter Deposit Amount: ")
            if amount.isnumeric() and (int(amount) != 0):
                amount = int(amount)
                if(caller.Loaned > 0):
                    will_pay = ''
                    while(True):
                        will_pay = input("Are you paying loans? (yes/no) --").lower()
                        if((will_pay != 'yes') and (will_pay != 'no')):
                            print("Invalid entry! Enter yes or no please")
                        else: break
                    if(will_pay == 'yes'):
                        curr_loan = caller.Loaned
                        caller.pay_loan(min(amount, curr_loan))
                        amount = max(0, (amount - curr_loan))
                if(amount>0): caller.Deposit(amount)
            else: print("Invalid Entry")

        elif c == '4':
            if(caller.Balance == 0):
                print("Transfer failed! Your balance is empty")
                continue

            acNumber = input("Enter reciever account number: ")
            if acNumber not in Bank()._users:
                print("Transfer failed! There is no such account in this bank")
            elif Bank()._users[acNumber][2] == 'admin':
                print("You can't transfer money to an Admin!")
            elif acNumber == caller.account:
                print("You can't transfer money to yourself!")
            else:
                while(True):
                    amount = input("Enter transfer amount: ")
                    if (not amount.isnumeric()) or (int(amount) > caller.Balance):
                        print("Invalid amount! Try again")
                        caller.show_Balance()
                    else:
                        caller.transfer(acNumber, int(amount))
                        break

        elif c == '5':
            caller.take_loan()

        elif c == '6':
            caller.check_history()

        elif c == '0':
            print("Logout Successful")
            break

        else:
            print("Invalid Entry! Try entering 0-6")

    while(signed == 'admin'):
        print("---------------------------")
        print("What would you like to do ?")
        print("[1] Check All users")
        print("[2] Delete a User account")
        print("[3] Check Total Bank Balance")
        print("[4] Check Loan amount")
        print("[5] Toggle loan feature")
        print("[0] Logout from Account")
        print("---------------------------")
        c = input("ENTRY: ")
        print("---------------------------")

        if c == '1':
            caller.show_all__users()
        elif c == '2':
            acNumber = input("Enter Account number to delete: ")
            if acNumber not in Bank()._users:
                print("Failed! There is no such account in this bank")
            elif Bank()._users[acNumber][2] == 'admin':
                print("Error! Can't delete an Admin account")
            else: caller.delete_user(acNumber)
        elif c == '3':
            caller.check_balance
        elif c == '4':
            caller.check_loaned
        elif c == '5':
            caller.toggle_loan
        elif c == '0':
            print("Logout Successful")
            break
        else:
            print("Invalid Entry! Try entering 0-5")
        