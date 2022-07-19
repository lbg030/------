n, m = map(int , input().split())

lst = [[0] * n for _ in range(m)]

k = 1
for i in range(n):
    for j in range(i,-1, -1):
        lst[i][j] = k
        k += 1

print(lst)