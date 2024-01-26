import random
from datetime import datetime
valid_chars = "0123456789_abcdefghijklmnopqrstuvwxyz"
secret_key = "********" # security for admin access

class Bank:
    _Bank_Balance = 0
    _Loan_Given = 0
    _Can_Loan = True
    _users = {}

    # generating unique semi-random account number:
    def generate_AC(self, mail):
        while(True):
            acNumber = mail.split("@")[0][:5] # personal part
            for c in range(5): # random part
                acNumber += random.choice(valid_chars)
            if acNumber not in self._users: return acNumber
    
    def create_account(self, acNumber, password, ac_type, instance):
        self._users[acNumber] = (instance, password, ac_type)

    def get_Instance(self, acNumber):
        return self._users[acNumber][0]


class User:
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

    def show_balance(self):
        print(f"Your Current Balance: {self.__balance}/-")

    def Deposit(self, amount):
        if not amount.isnumeric():
            print("* Invalid Entry")
            return
        amount = int(amount)
        if(self.__loaned_amount > 0): amount = self.pay_loan(amount)
        if(amount==0): return

        self.__balance += amount
        Bank._Bank_Balance += amount
        self.transaction('+', amount, 'Deposited')
        print(f"**{amount}/- Diposited Successfully!**")
        self.show_balance()

    def Withdraw(self, amount):
        if (not amount.isnumeric()) or (int(amount)==0):
            print("* Invalid Entry")
            return
        amount = int(amount)
        if(self.__balance < amount):
            print("* Withdrawal amount exceeded")
            self.show_balance()
        elif(Bank._Bank_Balance < amount):
            print("* Oops! We are bankrupt")
            if(Bank._Bank_Balance > 0):
                limit = min(Bank._Bank_Balance, self.__balance)
                print(f"Your current withdrawal limit: {limit}/-")
        else:
            self.__balance -= amount
            Bank._Bank_Balance -= amount
            self.transaction('-', amount, 'Withdrawn')
            print(f"**{amount}/- Withdrawn Successfully!**")
            self.show_balance()

    def take_loan(self):
        if(Bank._Can_Loan is True) and (Bank._Bank_Balance > 0):
            if(self.__loaned_time < 2):
                amount = int(input("Enter loan amount: "))
                if(Bank._Bank_Balance < amount):
                    print(f"* Sorry, current laon limit is {Bank._Bank_Balance}")
                else:
                    Bank._Loan_Given += amount
                    self.__loaned_time += 1
                    self.__loaned_amount += amount
                    self.__balance += amount
                    self.transaction('+', amount, 'Took Loan')
            else:
                print("* Denied! You've already taken max number of loans")
        else:
            print("**Sorry, This bank is not offering Loans at this moment!**")

    def pay_loan(self, amount) -> int:
        if amount == 0: return 0
        while(True):
            will_pay = input("Are you paying loans? (yes/no) --").lower()
            if((will_pay != 'yes') and (will_pay != 'no')):
                print("* Invalid entry! Enter yes or no please")
                continue
            if(will_pay == 'yes'):
                payment = min(amount, self.__loaned_amount)
                amount = max(0, (amount - self.__loaned_amount))
                self.__loaned_amount -= payment
                Bank._Loan_Given -= payment
                Bank._Bank_Balance += payment
                self.transaction('~', payment, 'Paid Loan')
                print(f"**{payment}/- Loan paid successfully!**")
                if(self.__loaned_amount != 0):
                    print(f"Now you have {self.__loaned_amount}/- loan left")
            return amount

    def transfer(self, acNumber):
        if acNumber not in Bank._users:
            print("* Transfer failed! There is no such account in this bank")
        elif Bank._users[acNumber][2] == 'admin':
            print("* You can't transfer money to an Admin!")
        elif acNumber == self.__acNumber:
            print("* You can't transfer money to yourself!")
        else:
            while(True):
                amount = input("Enter transfer amount: ")
                if (not amount.isnumeric()) or (int(amount)>self.__balance):
                    print("* Invalid amount! Try again")
                    self.show_balance()
                else:
                    amount = int(amount)
                    reciever = Bank._users[acNumber][0]
                    reciever.__balance += amount
                    reciever.transaction('+', amount, 'Transfered')
                    self.transaction('-', amount, 'Transfered')
                    self.__balance -= amount
                    print(f"**Successfully transfered {amount}/- to AC:{acNumber}**")
                    self.show_balance()

    def transaction(self, change, amount, note):
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.__transactions.append((time, change, amount, note))

    def check_history(self):
        if(len(self.__transactions)>0):
            counter = 1
            for Tn in self.__transactions:
                print(f"{counter}. {Tn[0]} [{Tn[3]}] {Tn[1]}{Tn[2]}/-")
                counter += 1
        else: print("* You haven't made any Transactions yet!")

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


class Admin:
    def __init__(self, acNumber, name, address, email):
        self.__acNumber = acNumber
        self.__name = name
        self.__address = address
        self.__email = email

    def show_all__users(self):
        for (key, val) in Bank._users.items():
            print(val[0])

    def delete_user(self, acNumber):
        if acNumber not in Bank._users:
            print("* Failed! There is no such account in this bank")
        elif Bank._users[acNumber][2] == 'admin':
            print("* Error! Can't delete an Admin account")
        else:
            ins = Bank._users[acNumber][0]
            cleared_loan = min(ins.__balance, ins.__loaned_amount)
            refund = max((ins.__balance - ins.__loaned_amount), 0)
            Bank._Loan_Given -= cleared_loan
            Bank._Bank_Balance -= refund
            del Bank._users[acNumber]
            print(f"**Account no. {acNumber} is Deleted successfully**")
            print(f"Loan cleared {cleared_loan} & Balance refunded {refund}")

    def check_balance(self):
        print("Current Bank Balance:", Bank._Bank_Balance)

    def check_loaned(self):
        print("Total Loans Given:", Bank._Loan_Given)

    def toggle_loan(self):
        Bank._Can_Loan = not Bank._Can_Loan
        if(Bank._Can_Loan is True):
            print("* Loans Turned ON: users can take loans now")
        else:
            print("* Loans Turned OFF: users can't take loans now")

    def __repr__(self) -> str:
        rep = f"""
Access Type     :Admin
Account Number  :{self.__acNumber}
User Name       :{self.__name}
User E-Mail     :{self.__email}
User Address    :{self.__address}
        """
        return rep

# Email validator for new account Registration:
def mail_validate() -> str:
    while(True):
        email = input("Enter a valid E-mail: ")
        if ('@' not in email) or ('.' not in email):
            print("* Invalid entry! Email must contain '@' and '.'")
        elif len(email.split("@")[0]) < 5:
            print("* Invalid entry! Too short")
        elif not all(c in valid_chars+'.@' for c in email):
            print('* Invalid character Error! Only use [a-z],[0-9],[@],[.],[_]')
        else:
            print("* Email Varification Successful")
            return email

# Login varificator:
def canLogin(acNumber, password) -> bool:
    return ((acNumber in Bank()._users) and (password == Bank()._users[acNumber][1]))


#######################################################################
op = Bank()
print("---------------------------")
print("Welcome to Terminal Banking")

# Main(outer) Repeating System:
while(True):
    caller = None # will store object of the required class
    signed = None # will indicate access type (user/admin)
    print("---------------------------")
    print("What would you like to do ?")
    print("[1] Create an Account")
    print("[2] Login to your Account")
    print("[3] Exit")
    print("---------------------------")
    cmd = input("ENTRY: ") 
    print("---------------------------")
    
    # Identifying User or Admin first, to login/register/interact accordingly:
    if(cmd=='1' or cmd=='2'):
        while(signed is None):
            ac = input("Access Type (USER or ADMIN): ").lower()
            if(ac=='user' or ac=='admin'): signed = ac
            else:
                print("* Invalid entry! Try again")
        if(signed == 'admin'):
            access_key = input("Enter Admin Access Key: ")
            if(access_key != secret_key):
                print("* Access Denied! Invalid Key")
                continue

    # Creating a new Account:
    if(cmd=='1'):
        name = input("Enter you Name: ")
        address = input("Enter your Address: ")
        email = mail_validate()
        acNumber = op.generate_AC(email)
        if(signed == 'user'):
            while(True):
                acType = input("Account Type (Savings/Current): ").lower()
                if(acType!='savings' and acType!='current'):
                    print("* Invalid account type. Enter Savings or Current")
                else:
                    caller = User(acNumber, name, address, email, acType)
                    break
        else: caller = Admin(acNumber, name, address, email)
        password = input("Enter new Password: ")
        op.create_account(acNumber, password, signed, caller)
        print("**Account created Successfully**")
        print("Signed in to AC:", acNumber)

    # Logging into an Existing account:
    elif(cmd=='2'):
        print("Enter Valid Login Info -")
        acNumber = input("Account Number: ")
        password = input("Password: ")
        if canLogin(acNumber, password):
            print("Signed in to AC:", acNumber)
            caller = op.get_Instance(acNumber)
        else:
            print("* Invalid AC number or password! Please try again.")
            continue
    
    # Program Terminator:
    elif(cmd=='3'):
        print("Thanks for visiting Terminal Banking, Come again\n")
        break

    # Invalid manu-input Handing:
    else:
        print("* Invalid Entry! Try Entering 1-3\n")
        continue

    # User's repeating Menu:
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
            caller.show_balance()
        elif c == '2':
            amount = input("Enter withdrawal Amount: ")
            caller.Withdraw(amount)
        elif c == '3':
            amount = input("Enter Deposit Amount: ")
            caller.Deposit(amount)
        elif c == '4':
            if(caller.Balance == 0):
                print("* Transfer failed! Your balance is empty")
                continue
            acNumber = input("Enter reciever account number: ")
            caller.transfer(acNumber)
        elif c == '5':
            caller.take_loan()
        elif c == '6':
            caller.check_history()
        elif c == '0':
            print("**Logout Successful**")
            break
        else: print("* Invalid Entry! Try entering 0-6")

    # Admin's repeating Menu:
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
            caller.delete_user(acNumber)
        elif c == '3':
            caller.check_balance()
        elif c == '4':
            caller.check_loaned()
        elif c == '5':
            caller.toggle_loan()
        elif c == '0':
            print("**Logout Successful**")
            break
        else: print("* Invalid Entry! Try entering 0-5")
        