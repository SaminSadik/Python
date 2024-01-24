"""
TODO:
* User transaction history
* Admin show all users
* generate account number
* connect user/admin menu interactions
"""

class Bank:
    Bank_Balance = 0
    Loan_Given = 0
    Can_Loan = True
    users = {}
    def __init__(self) -> None:
        pass

class User(Bank):
    def __init__(self, a,b,c,d,e,f):
        self.__ac_number = a
        self.name = b
        self.address = c
        self.email = d
        self.__password = e
        self.ac_type = f
        self.__balance = 0
        self._loaned = 0
        self._transactions = {}

    @property
    def Balance(self):
        print(f"Your Current Balance: {self.__balance}")

    def Deposit(self, amount):
        self.__balance += amount
        super().Bank_Balance += amount
        print(f"{amount}/- Diposited Successfully!")
        self.Balance

    def Withdraw(self, amount):
        if(super().Bank_Balance < amount):
            print("Oops! We are bankrupt")
        elif(self.__balance >= amount):
            self.__balance -= amount
            super().Bank_Balance -= amount
            print(f"{amount}/- Withdrawn Successfully!")
            self.Balance
        else:
            print("Withdrawal amount exceeded")
            self.Balance

    def take_loan(self, amount):
        if(super().Can_Loan is True):
            while(super().Bank_Balance < amount):
                print(f"Sorry, current laon limit is {super().Bank_Balance}")
                amount = int(input("New Loan Amount: "))
                if(amount < 1):
                    print("Loan Request is Cancelled")
                    return

            if(self._loaned < 2):
                self.Deposit(amount)
                self._loaned += 1
                super().Loan_Given += amount
                super().Bank_Balance -= amount
            else:
                print("Denied! You've already taken max number of loans")
        else:
            print("Sorry, This bank is not offering Loans at this moment!")

    def transfer(self, ac_number, amount):
        reciever = super().users[ac_number][0]
        reciever.Deposit(amount)
        print(f"Successfully transfered {amount}/- to AC:{ac_number}")
        self.Balance

    def check_history(self):
        pass


class Admin(Bank):
    def __init__(self, a,b,c,d,e):
        self.__ac_number = a
        self.name = b
        self.address = c
        self.email = d
        self.__password = e

    def show_all_users(self):
        pass

    def delete_user(self, acc_number):
        if super().users[acc_number][2] == 'admin':
            print("Error! Can't delete another Admin account")
        else:
            del super().users[acc_number]
            print(f"Account no. {acc_number} is Deleted successfully")

    @property
    def check_balance():
        print("Current Bank Balance:", super().Bank_Balance)

    @property
    def check_loaned():
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
        ac_type = None
        while(signed is 'user'):
            ac_type = input("Account Type (Savings/Current): ").lower()
            if(ac_type!='savings' and ac_type!='current'):
                print("Invalid account type. Enter Savings or Current")
            else: break
        _password = input("Enter new Password: ")
        ac_number = generateAC()

        if(signed is 'admin'):
            caller = Admin(ac_number, name, address, email, _password)
        else:
            caller = User(ac_number, name, address, email, _password, ac_type)

        op.users[ac_number] = [caller, _password, signed]
        print("Account created Successfully!")
        print("Signed in to AC:", ac_no)
        print("---------------------------")

    elif(cmd=='2'):
        print("Enter Valid Login Info -")
        ac_no = input("Account Number: ")
        password = input("Password: ")
        if (ac_no not in op.users) or (password != op.users[ac_no][1]):
            print("Invalid AC number or password! Please try again.")
        else:
            print("Signed in to AC:", ac_no)
            caller = op.users[ac_no][0]
        
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
        