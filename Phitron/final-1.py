class User:
    pass

class Admin:
    pass

def generateAC():
    pass

print("---------------------------")
print("Welcome to Terminal Banking")
print("---------------------------")

cmd = '0'
signed = 'none'
users = {}

while(True):
    print("What would you like to do ?")
    if(signed is 'none'):
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
        name = input("Enter you Name: ")
        address = input("Enter your Address: ")
        if(signed is 'user'):
            ac_type = input("Account Type (Savings/Current): ").lower()
            while(ac_type!='savings' or ac_type!='current'):
                print("Invalid account type. Enter Savings or Current")
                ac_type = input("Account Type (Savings/Current): ").lower()
        email = input("Enter a valid E-mail: ")
        while email in users:
            print("Email already exists! Please try again.")
            email = input("Enter a valid E-mail: ")
        _password = input("Enter a unique Password: ")
        ac_number = generateAC()
        if(signed is 'admin'):
            users[email] = Admin(signed, ac_number, name, address, email, _password)
        else:
            users[email] = User(signed, ac_number, name, address, ac_type, email, _password)
        print("Account created Successfully!")
        print(f"Account Number: {ac_number}")
        print("---------------------------")

    elif(cmd=='2'):
        print("Enter Valid Login Info:")
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
        pass

    while(signed == 'admin'):
        pass
        
