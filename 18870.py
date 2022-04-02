from sys import stdin
n = int(input())
li = list(map(int, stdin.readline().rstrip().split()))
print(li)
minimum = min(li)
idx = li.index(minimum)

for x in li:
    if x == li[idx]:
        x = 0
    li[idx] = 0
