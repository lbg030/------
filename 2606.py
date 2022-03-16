n = int(input())
t = int(input())
s = [[0] * n for i in range(n)]
visit = [0 for i in range(n)]
for i in range(t):
    a, b = map(int, input().split())
    s[a - 1][b - 1] = 1
    s[b - 1][a - 1] = 1


def dfs(v):
    visit[v] = 1
    for i in range(n):
        if s[v][i] == 1 and visit[i] == 0:
            dfs(i)


print(f"s= {s}")
print(f"visit = {visit}")
dfs(0)
cnt = 0
for i in range(1, n):
    if visit[i] == 1:
        cnt += 1
print(cnt)
