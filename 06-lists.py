 #! List basics:
numbers = [1, 2, 3, 4, 5] #this is a list or array
print(numbers,'\n')

# python simulataniously has two types of indexing:
for i in range(5): # forward index: 0 to size-1 (normal)
    print(f"[{i}] = {numbers[i]}")
for i in range(-5, 0): # backward index: -size to -1
    print(f"[{i}] = {numbers[i]}")
print()

 #! Slicing Lists (kind of subarray):
print(numbers[1:3]) # subarray from (1st index) to (2nd index)-1
print(numbers[-5:-2:2]) # 3rd value(optional) is steps(+=/-=)
print(numbers[:3]) # 1st value is by default the starting index
print(numbers[2:]) # 2nd value is by default the last index
print(numbers[::-1]) # shortcut to reverse the list

 #! Basic list methods:
numbers.append(6) # inserts the value at the end of the list
print('\nPost-Appended List:',numbers)

numbers.insert(1, 12) # 1st parameter index, 2nd parameter value
# inserts value on the index, pushes from that index till the end to right
print('Post-Inserted List:',numbers)

numbers.remove(12) # removes the value, will throw error if not in the list
print('Post-Removed  List:',numbers)
if 100 in numbers: # checking before removing to avoid errors
    numbers.remove(100)
    print('Post-Removed List:', numbers)
else: print("Errors Avoided, Non-existing Not-removed")

last = numbers.pop() # removes last elements as well as returns it
print(f"After Popping {last}, List: {numbers}\n")

idx = numbers.index(3) # shows index of given value if it's in the list
print(f"3 is at index [{idx}]") # shows forward index by default
if 10 in numbers: # avoiding errors when value isn't in the list
    i = numbers.index(10,1,3) # searching in a range of index
    print(f"10 is at index [{i}]")
else: print("10 is not in the list\n")

numbers.reverse()
print(f"Reversed List: {numbers}")

numbers.sort()
print(f"Sorted   List: {numbers}")

cents = numbers.count(100) # counts the no. of given value in the list
print(f"100 appeared {cents} times in the list!")

print(f"\nBefore clearing: {numbers}")
numbers.clear() # clears whole list
print(f"After clearing: {numbers}\n")

 #! Shallow Copying list:
numbers = [1, 2, 3, 4, 5]
copied1 = numbers # Reference Copy
copied1.append(6) # changes in the copied list will apply to the original
print(f"Original: {numbers}\n Copied:  {copied1}")

copied2 = numbers[:] # Slicing Copy
copied2[0] = 10; # changes in the copied list doesn't affect the original
print(f"Original: {numbers}\n Copied: {copied2}")

copied3 = numbers.copy() # using copy() method
copied3[5] = 10; # changes in the copied list doesn't affect the original
print(f"Original: {numbers}\n Copied: {copied3}\n")
# Deep copy exists but not going too Deep for now

 #! Comprehension / Shortcut (not recommended):
filtered = [] # empty list

for n in numbers:
    if (n%2) and n<5:
        for i in range(3):
            filtered.append([n, i])
print("Usual Filtered:", filtered)

# following 2 lines does same thing as above 5 lines, but less readable
short_filtered = [[n,i] for n in numbers if(n%2) if(n<5) for i in range(3)]
print("Short Filtered:", short_filtered)