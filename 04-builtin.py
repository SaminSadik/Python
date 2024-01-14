x = input("Enter X : ") # taking user input
print("User:", x, end = " ; ") # showing output
# if end is not specified, it's "\n" by default

print(type(x)) # identify the data type of variable
x = int(x); print(type(x)) # convert to integer
# similartly str(), chr(), float() are used for convertion

for i in range(0, 10, 1): # same as range(0,10) or range(10)
    print(i, end=" ")
print() # used as a line break
# 1st value, start of range, is 0 by default, it's included in the range
# 2nd value (must) is end of range +1, so it's not included in the range
# Optional 3rd value, steps(increment/decrement) is +1 by default
# descending range work with -ve steps only & ascending with +ve steps
for i in range(10, 0, -2): print(i, end=" ")
print()

numbers = [2, 4, 6, 8]
for idx, val in enumerate(numbers):
    print(f'Index {idx} : {val}')
# enumerate returns pairs of (index,element) from a list

print(max(1, 88, 22, 99, 5)) # gives the maximum value
print(min(99, 5, 22, 1, 88)) # gives the minimum value
# can also pass an array as parameter in min & max as well

print(len([9, 8, 6])) # counts the length of array/list
print(sum({1,2,3,4,5})) # calculates the sum of list/array

print(abs(10-100)) # return the absolute value (+ve)