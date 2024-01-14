# Set is a collection of Unique items in {}

alist = [101, 2, 31, 2, 5, 4, 101, 15]
print("List:", alist)
set1 = set(alist) # Doesn't maintain given order of occurance
print("Converted Set:", set1) # Removes Duplicates

set2 = {3,5,10,15,16,30,31,101,1} # creating set
set3 = set() # creating empty set
print(set3, "is", type(set3)) # shows set as type
print(f"Size of {set2} is {len(set2)}\n") # size of set with len()

set1.add(30) # adds an element randomly in the set, if not duplicate
print("Set after Addition:", set1)
set1.remove(2) # removes the element from set
print("Set after Removal :", set1)
set1.pop() # removes a random element from set
print("Set after Popping :", end=" ")
for element in set1: # can be accessed in loop with 'in'
    print(element, end=" ")
# check if specific element is in the set using 'in'
if 15 not in set1: print("\t{Where did 15 go?}\n")
else: print("\t{15 exists in the set}\n")

# can't access or modify set elements using index (position)
# print(set1[1]) won't work

print(f"{set1} is subset of {set2}", end=": ")
print(set1.issubset(set2)) # if all elements of left exist in right
print(f"{set2} is super set of {set1}", end=": ")
print(set2.issuperset(set1)) # if all elements of right exist in left
print(f"{set1} is disjoint set of {set2}", end=": ")
print(set1.isdisjoint(set2)) # if both set have no element in common

print(f"\nBefore clearing: {set2}")
set2.clear() # clears whole set
print(f"After clearing: {set2}\n")

set4 = {'a', 'b', 'c'}
set5 = {'e', 'd', 'a'}
# Following 3 operation returns a new set, don't modify original sets
print('Union:',set4 | set5, end=" -> ")
# The above line is the shortcut for the following line:
print(set4.union(set5))
# Union is combining the elements both sets, ignoring the duplicates
print('Intersection:',set4 & set5, end=" -> ")
# The above line is the shortcut for the following line:
print(set4.intersection(set5))
# Intersection is only elements that are common in both sets
print('Difference:',set4 - set5, end=" -> ")
# The above line is the shortcut for the following line:
print(set4.difference(set5))
# Difference is the elements of left set that aren't in right set
print()

# Following 3 methods update the original set, not return a new set
set4.update(set5) # operation is same as union
print("Updated Union Set:", set4)
set4.intersection_update(set5) # operation is same as intersection
print("Updated Intersection Set:", set4)
set4.difference_update(set5) # operation is same as difference
print("Updated Difference Set:", set4, "\n")