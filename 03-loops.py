 #! While Loop:
num = 10
while num > 0: # loop will iterate while the condition is true
    print(num)
    num -= 1
print() # indentation must be maintained, just like conditionals

 #! Continue & Break:
while num < 10:
    num += 1
    if num==4: continue # continue skips current iteration
    if num==8: break # break ends the loop
    print(num)
print()

 #! For Loop:
text = "Hi Python"
for char in text:
    print(char)
print()

 #! enumerate:
for i, e in enumerate(text): print('Index',i,':',e)
# enumerate returns pairs of (index,element) from a list
print()

 #! range:
sum = 0
for i in range(2, 10, 2): # a range from 2 to 10-1, in +2 increments
    sum += i
    if(sum == 2): print("Let's sum small evens")
# 3rd value steps(optional) is basically increment or decrement(if -ve)
print("Result =", sum, '\n')

for i in range(5): print(i) # same as range(0,5)
print() # starting value is 0 by default if not specified

 #* zip() function can loop over two or more sequences at the same time! 