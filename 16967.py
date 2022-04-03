n, m, x, y = map(int, input().split())
a = [[0] * m for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n+x)]

print(a, b)
