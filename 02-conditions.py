n1 = 3; n2 = 11 # to separate statements in same line ; can still be used
 #! Basic Operators
# basic addition(+) & subtraction(-):
print(n1,'+',n2,'=', n1+n2 ,';',n1,'-',n2,'=', n1-n2)
# multiplication (*) & power (**):
print(n1,'x',n2,'=', n1*n2 ,';',n1,'^ 2 =', n1**2)
# Full division result (/) & Integer Division result (//):
print(n2,'/',n1,'=', n2/n1 ,'or', n2//n1)
# Remainder of division (%):
n2 %= n1; print('& Remainder =', n2)
# [var = var op val] => [var op= val] (shorthand)
# increment(++) & decrement(--) aren't available in python as operators

a = int(input("\nEnter a Number: ")) # convert str to int while taking input
 #! Basic if-else conditions
if a>5: print(a,"is greater than 5") # single statement can be on the same line
else: # for multiple statements, indentation (same no. of spaces) is compulsory
    print(a, "is not greater than 5")
    print(a, "is less than 8 aswell")
 #! Basic if-elseif-else tree
if a<=10:
    print(a, 'is less than 11')
elif a<100: # there can be as many elif (elseif is elif in python) as needed
    print(a, 'is less than 100')
elif a==8: # if a condition of the block is true, others below are skipped
    print(a, 'is infinity?')
else: print(a, 'is quite big')
 #! if & indentation
if (a == 8): # spaces & () is fine 
    print(a, 'is INFINITY') # there can be no elif or else
print("Different Indentation, Not in the conditional block\n")

 #! nested conditions 
flag = False
if not flag: # same as, if !flag:
    print('Start of Nest')
    if (flag is True) and (flag == True): print('flag is True')
    # only true if both conditions before & after 'and' are true
    # is & == are same
    # 'and' is used instead of && in python
    else:
        print('flag is False')
        if (flag != True) or (flag is not True):
            print('flag is not True')
        # only false if both conditions before & after 'or' are false
        # is not & != are same
        # 'or' is used instead of || in python
        else: print('flag is not False')
    print('End of Nest')
else: print('No Nest')
print('------------')