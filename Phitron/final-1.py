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
        super().users[self.__ac_number] = [
            self.name, self.address, self.email,
            self.__password, self.ac_type
        ]

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
            print("Oops! Bank is bankrupt")
        elif(self.__balance >= amount):
            self.__balance -= amount
            super().Bank_Balance -= amount
            print(f"{amount}/- Withdrawn Successfully!")
            self.Balance
        else:
            print("Withdrawal amount exceeded")
            self.Balance

    def take_loan(self, amount):
        if(super().Can_Loan is True) and (super().Bank_Balance >= amount):
            if(self._loaned < 2):
                self.Deposit(amount)
                self._loaned += 1
                super().Loan_Given += amount
                super().Bank_Balance -= amount
        else:
            print("Sorry, This bank is not offering Loans at this moment!")

    def pay_loan(self, amount):
        pass

    def transfer(self, ac_number, amount):
        pass

    def check_history(self):
        pass


class Admin(Bank):
    def __init__(self, a,b,c,d,e):
        self.__ac_number = a
        self.name = b
        self.address = c
        self.email = d
        self.__password = e
        super().users[self.__ac_number] = [
            self.name, self.address,
            self.email, self.__password, None
        ]

def generateAC():
    pass

print("---------------------------")
print("Welcome to Terminal Banking")

cmd = '0'
signed = 'none'
op = Bank()

while(True):
    caller = None
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
        while(signed is 'none'):
            ac = input("Are you USER or ADMIN: ").lower()
            if(ac=='user' or ac=='admin'): signed = ac
            else:
                print("Invalid entry! Try again")

    if(cmd=='1'):
        email = input("Enter a valid E-mail: ")
        if email in op.users:
            print("Email already exists! Please try again.")
            continue
        name = input("Enter you Name: ")
        address = input("Enter your Address: ")
        if(signed is 'user'):
            while(True):
                ac_type = input("Account Type (Savings/Current): ").lower()
                if(ac_type!='savings' or ac_type!='current'):
                    print("Invalid account type. Enter Savings or Current")
                else: break
        _password = input("Enter a unique Password: ")
        ac_number = generateAC()
        if(signed is 'admin'):
            caller = Admin(ac_number, name, address, email, _password)
        else:
            caller = User(ac_number, name, address, email, _password, ac_type)
        print("Account created Successfully!")
        print(f"Account Number: {ac_number}")
        print("---------------------------")

    elif(cmd=='2'):
        print("Enter Valid Login Info -")
        ac_no = input("Account Number: ")
        password = input("Password: ")
        if (ac_no not in op.users) or (password != op.users[ac_no][3]):
            print("Invalid email or password! Please try again.")
        else:
            print("Login Successful: Account No.", ac_no)
        
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
        print("[6] Payback Loan")
        print("[7] Check Transaction History")
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
        elif c == '7':
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
        
