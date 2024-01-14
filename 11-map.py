 #! MAP:
aList = [1, 12, 71, 100, 8] # iterable list
def square(x): return x**2 # function

aMap = map(square, aList) # map takes a function & an iterable
# map applies the function in the whole iterable(generally list)
print(aMap) # by default returns a map object
print(list(aMap)) # converting into list is standard to see

 #! FILTER:
# filter takes a boolean function & an iterable
newList = filter(lambda x: x<50, aList) # used a lambra function
# iterable elements not fulfilling condition are filtered out
print(newList) # also returns an object & needs to be converted
print(list(newList))

 #! REDUCE:
from functools import reduce # needs to be imported
reduced = reduce(lambda x,y: x*y, aList) # takes a function & iterable
# applies the function to the iterable until it's an accumulated result
print(f"Multiplication of {aList} is {reduced}")