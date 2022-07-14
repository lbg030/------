from sys import stdin
from collections import deque

n = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(n-1):
    x, y = map(int, stdin.readline().rstrip().split())
    graph[x][y] = graph[y][x] = 1
    
    