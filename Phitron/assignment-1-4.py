 #? https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P

n = int(input())
a = list(map(int, input().split()))

ans, flag = 0, True
while flag is True:
    for i in range(len(a)):
        if(a[i]%2):
            flag = False
            break
        a[i] //= 2
    if flag is True: ans += 1

print(ans)
