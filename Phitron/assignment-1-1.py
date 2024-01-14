 #? https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S

s = input()
new = ""
l, r = 0, 0

for c in s:
    if c == 'R': r += 1
    else: l += 1
    new += c
    if (r>0) and (l==r):
        new += " "
        l, r = 0, 0

ans = new.split()
print(len(ans))
for x in ans: print(x)
