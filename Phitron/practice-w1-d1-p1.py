 #? https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Q

t = int(input())
for i in range(t):
    n = input()
    for c in n[::-1]:
        print(c, end=" ")
    print()

""" 
t = int(input())
for i in range(t):
    n = int(input())
    if(n==0):
        print(0)
        continue
    res = []
    while n>0:
        res.append(n%10)
        n //= 10
    for num in res: print(num, end=" ")
    print()
"""
