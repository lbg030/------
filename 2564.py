n,m = map(int, input().split())
k = int(input())

block = [[0] * n for _ in range(m)]

for _ in range(k):
    x,y = map(int, input().split())