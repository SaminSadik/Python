 #? https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/F

x, n = input().split()
x = int(x)
n = int(n)
s = 0
for i in range(2,n+1,2): s += (x**i)
print(s)