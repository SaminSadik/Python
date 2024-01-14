 #? https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Z

k, s = input().split()
k, s = int(k), int(s)

Count = 0
for x in range(0,k+1):
    for y in range(0,k+1):
        if 0 <= s-x-y <= k: Count += 1
print(Count)