 #? https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Y

n = int(input())

fib = [0]
for i in range(1,n+1):
    if(i==1): fib.append(0)
    elif(i==2): fib.append(1)
    else: fib.append(fib[i-1]+fib[i-2])
    print(fib[i], end=" ")
