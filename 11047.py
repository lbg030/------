from sys import stdin

n, m = map(int, input().split())
li = []
count = 0

for i in range(n):
    li.append(int(input()))

for j in range(len(li)-1, -1, -1):
    res = m // li[j]
    m = m % li[j]
    if(res >= 1):
        count += res

print(count)
