def func(num): print(num)
func(10)

# Function format >> def name(parameters): [indent] statements...
def Sum(a, b):
    ans = a + b
    return ans # returns the value, type is automatic

num = func(Sum(8,80))
print(num) # if nothing's returned it's 'none' by default
num = Sum(80,8)
func(num) ;print()

 #! Arguments / Optional Parameters:
def show(n1, n2, n3, n4=0, n5=0): print(n1,n2,n3,n4,n5)
# if optional parameters are not given they will be 0, n4 & n5 here
show(4, 3, 2, 1)

def dump_any(*args): # tuple (*something) is like a list
    print(args) # prints the whole tuple in () separated by comma
    for i in args: print(i)
    # tuple can be iterated like with loop like other lists
dump_any(10, 20, 30) # tuple will take any number of parameter

def dump_some(p1, p2, *args):
    print(args) # tuple is like optional parameter, it may get none
    print(p1, p2) # but fixed parameters like these must be given
dump_some(40,50) ;print()

 #! Key arguments:
def full_name(first, last): print(f"Full Name: {first} {last}")
full_name(last='Sadik', first='Samin') # use keys instead of order

def key_it(k1, k2, *args, **kargs):
    # access a single value in kargs through its key:
    print(f"{k1}, {k2}, {args}, {kargs['xtra2']}")
    print(kargs) # print the whole kargs with all keys & values
    # iterate through kargs to get pairs of (key,value) from it:
    for k, v in kargs.items(): print(k +" = "+ v)
# kargs(**) take any number of parameters but with key(like index of map)
key_it('A', 'B', 'c', xtra1='C', xtra2='D') ;print()

 #! Return multiple:
def return_all(a, b):
    add = a+b
    sub = a-b
    mod = a%b
    return add, sub, mod # return multiple values as tuple
print(return_all(50,8))
# return multiple values as list
def return_list(a,b): return [a+b, a-b, a%b]
print(return_list(50,8))

 #! Scope:
known = 100
def check_scope(key, val):
    global known
    # global variables can be used locally, but can't be modified as usual
    print('Current:', known)

    relation = f"{key} = {val}"
    # these local variables can't be used outside function's scope
    print(relation)

    # 'global' keyword need to be used at the start of function to modify it
    known -= val

check_scope('item', 10)
# print(key, val, relation) # won't work as those are local to their function
print("Final: ", known) ;print()

 #! Lambda (shorthand function):
def add(a,b):
    return a+b
print("Small Function: 1+99 =",add(1,99))
# Write these type of small function in one line (using lambda):
AplusB = lambda a,b : a+b
# format>> function-Name = lambda parameters : returning-operation
print("1-liner Lambda: 1+99 =",AplusB(1,99))