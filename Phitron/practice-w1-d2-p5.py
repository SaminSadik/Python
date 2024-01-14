 #? https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/Q

s = input().split()
i = len(s)
for word in s:
    print(word[::-1], end="")
    i -= 1
    if(i>0): print(end=" ")