 #! 3 types of string quotation:
text1 = "Samin's Code"
print(text1)
text2 = 'San\'s Code' # escape(\) is needed for some characters
print(text2)
text3 = """ 
    This is not a Comment here
    It's a mutlti-line String!
""" # counts all the whitespace & lines as it is
print(text3)

 #! Indexing & Iteration:
for i in range(-10,0): # also have both indexing simultaniously
    print(f"Index [{i}]:\t {text2[i]}")
print()
for idx, char in enumerate(text2): # can be iterated normally
    print(f"Index [{idx}]:\t {char}")
print()

 #! Slicing (kind of substrings):
print("Sliced: ",text1[1:11:3]) # same as in lists
print("Reversed: ",text1[::-1]) # shortcut to reverse the string
print()

 #! Searching with conditional:
if 'Code' in text2: # easily search in string
    print('Code is in', text2)
else: print("No Code Here")
if 'not' in text3[25:]: # can search in specific portion
    print('not here')
else: print('no not here')

 #! Appending w/o Method:
text1 = text1 + " is " + text2
print(text1, "\n")

 #! Common Methods:
demoTxt = "thiS iS a DeMo"
print("UPPERcased: ", demoTxt.upper()) # uppercases whole string
# isupper() returns True if whole sting's uppercase
print("lowerCASED: ", demoTxt.lower()) # lowercases whole string like casefold()
# islower() returns True if whole sting's lowercase
print('Capitalized:', demoTxt.capitalize()) # capitalizes 1st letter
print('And, Titled:', demoTxt.title()) # capitalizes 1st letter of each word
# istitle() returns True if 1st letter of every word is capital

n1, n2= "123", "123 .00"
if n1.isnumeric(): print(n1, 'is Numeric')
# isNumeric returns True if all the characters are digits or numeric
if not n2.isnumeric(): print(n2, 'is not Numeric\n') # space or . are not numeric
# similarly isalpha works for alphabets, again space or symbols are not acceptable
if demoTxt.isalpha(): print(demoTxt, 'is ALPHA')

demoTxt = text3[:]
Countis = demoTxt.count('is') # count occurences in string
print(f"there is {Countis} 'is' in {demoTxt}")
Findis = demoTxt.find('is') # finds 1st index of occurance
print(f"'is' first found at index[{Findis}]")
Findis = demoTxt.rfind('is') # finds last index of occurance
print(f"'is' last found at index[{Findis}]")
# unlike index(), find() returns -1 instead of error if not found
noIndex = demoTxt.find("san") # same applies for rindex() & rfind()
print(f"san not found as find() returned {noIndex}\n")

demoTxt = "Samin Sadik, Khan, San"
print(demoTxt,'->',demoTxt.split()) # splits the string
partitions = input("Enter a few thing separated by comma: ").split(",",1)
# 1st parameter is separator, 2nd parameter is maxsplit, both are optional
print(partitions,"\n") # Actually, no. of splits = maxsplits+1
# Separator specifies what splits the string, by default any whitespaces
# maxsplits specifies no. of slits to do, by default -1(means all possible)

demoTxt = "This is San not san"
print("Original:", demoTxt)
demoTxt = demoTxt.replace(' San', ' Sadik')
print("Modified:", demoTxt)
# replaces 1st substring with the 2nd substring, in the main string
demoTxt = demoTxt.replace('s', ' ', 2) # 3rd parameter (count) is optional
# count specifies how many occurances to replace, by default all
print("More CNG:", demoTxt)
# Unlike lists, Sting is not mutable / changable, e.g.
# text2[4] = 'r' # won't change the string, but throw an eroor

print("BO8\t->", "BO8".zfill(5))
# makes the string of given size(5 here) by adding zeros(0) at the start
print("1.00\t->", "1.00".zfill(5))
# if the string size is already => given zfill size, no 0 will be added
print("Z O S\t->", "Z O S".zfill(5)) ;print()

print('Centered:','SAN'.center(10))
# centers the string within the given size by adding spaces before & after
print('Centered:','SAN'.center(10,'-'))
# 2nd parameter is optional, changes the filling character from a space
print('Centered:','SAmiNsadik'.center(10,'-')) ;print()
# if original string size => given center size, the method doesn't apply

demoTxt = "Hence, {name} gets {number} points"
# atleast 1 {forrmattable} required
print(demoTxt.format(name="'String'", number="[99]"), end =" ")
# if there's no {keyword}, then format() doesn't need keyword aswell
demoTxt = "out of {}.".format(100)
print(demoTxt)