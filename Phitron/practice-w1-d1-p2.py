 #? https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/S

test = int(input())
for case in range(test):
    nums = input().split()
    x = int(nums[0])
    y = int(nums[1])
    Sum = 0
    for n in range(min(x,y)+1, max(x,y)):
        if n%2: Sum += n
    print(Sum)