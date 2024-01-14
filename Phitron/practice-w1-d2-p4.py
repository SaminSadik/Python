 #? https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/Y

n, q = map(int, input().split())
a = list(map(int, input().split()))

pre_sum = [0]
for i in range(n):
    pre_sum.append(pre_sum[-1]+a[i])

for i in range(q):
    l, r = map(int, input().split())
    print(pre_sum[r]-pre_sum[l-1])