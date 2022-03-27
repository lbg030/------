from sys import stdin

n, m = map(int, input().split())

k = list(map(int, stdin.readline().split()))
res = []
for i in range(n):
    if(k[i] < m):
        res.append(k[i])

print(*res)
