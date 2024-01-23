class User:
    def __init__(self, a,b,c,d,e,f,g,h,i):
        self._access =  a
        self._name = b
        self.__address = c
        self._ac_type = d
        self._email = e
        self.__pass = f
        self._ac_number = g
        self._balance = h
        self._loaned = i

class Admin:
    def __init__(self, a,b,c,d,e,f):
        self._access =  a
        self._name = b
        self.__address = c
        self._email = d
        self.__pass = e
        self._ac_number = f

def generateAC():
    pass

print("---------------------------")
print("Welcome to Terminal Banking")

cmd = '0'
signed = 'none'
users = {}

while(True):
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
        if email in users:
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
        balance = 0
        loaned = 0
        ac_number = generateAC()
        if(signed is 'admin'):
            users[email] = Admin(signed, name, address, email, _password, ac_number)
        else:
            users[email] = User(signed, name, address, ac_type, email, _password, ac_number, balance, loaned)
        print("Account created Successfully!")
        print(f"Account Number: {ac_number}")
        print("---------------------------")

    elif(cmd=='2'):
        print("Enter Valid Login Info -")
        email = input("E-mail: ")
        _password = input("Password: ")
        if (email not in users) or (_password != users[email._password]):
            print("Invalid email or password! Please try again.")
        else:
            print("Login Successful: Account No.", users[email].ac_number)
        
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
        print("[5] Check Transaction History")
        print("[6] Apply for Loan")
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
        
