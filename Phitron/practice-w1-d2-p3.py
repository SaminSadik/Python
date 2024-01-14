 #? https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M

n = int(input())
a = list(map(int, input().split()))

mni = a.index(min(a))
mxi = a.index(max(a))

a[mni], a[mxi] = a[mxi], a[mni]
for i in a: print(i, end=" ")