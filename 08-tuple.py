Tupl = 'Not String',
print(Tupl, type(Tupl)) # because of comma, it became a tuple

Tupl = 'A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8'
print(Tupl)

print(Tupl[0],'=',Tupl[-8]) # also have 2 types of indexing
print(Tupl[7:1:-2]) # slicing also work same as lists

for x in Tupl: print(x, end=" ") # simply iterable
print(f"[Total: {len(Tupl)}]") # shows the size of tuple

def ReturnMultuple(n):
    return n, n+1, n+2
# function returns multiples separated by , or inside() as tuple
print("Returned as Tuple:",ReturnMultuple(1))

# Tuple can be a list of different types of variables/lists
list_of_lists = (['A1','D4',7], Tupl)
print(list_of_lists, f"[Size: {len(list_of_lists)}]")
# list_of_lists[0] = [4, 5, 6] # can't modify tuple elements like this
list_of_lists[0][2] = 'G7'
print(list_of_lists) # can modify mutable elements of tuple elements

Tupl = (1,2,3,2,3,2,0,1,5)
print(f'No. of 2 in {Tupl}: ', Tupl.count(2)) # counts occurances

i = Tupl.index(0) # finds the first index of first occurance
print('0 found at Index', i)
# checking if specific element is in the tuple:
if 10 in Tupl[1:7]: # if not found, index() would've thrown error
    print('0 found at Index', Tupl.index(10, 1, 7)) # search in range
# 2nd (starting index) & 3rd (ending index) parameters are optional
else: print('10 is not Found, But Errors Avoided')

 # TODO: add important methods like append()