 #? https://atcoder.jp/contests/arc087/tasks/arc087_a

n = int(input())
a = list(map(int, input().split()))

freq = {}
for i in a:
    if i in freq: freq[i] += 1
    else: freq[i] = 1

removed = 0
for element, occurred in freq.items():
    removed += occurred
    if occurred>=element: removed -= element

print(removed)