n,m= map(int, input().split())
lst1=[list(map(int, input().split())) for _ in range(n)]
lst2=[list(map(int, input().split())) for _ in range(n)]

result = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        result[i][j] = lst1[i][j] + lst2[i][j]

for x in result:
    print(*x)