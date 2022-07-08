from sys import stdin

n, m = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)] #값 저장 그래프
BellmanFord = graph = [[0] * (n+1) for _ in range(n+1)] #1에서 최단거리를 구하기 위한 그래프
check = [[False] * (n+1) for _ in range(n+1)] #방문 여부 // 0 으로 체크하면 돼서 필요 없을수도

for _ in range(m):
    x,y,k = map(int, stdin.readline().rstrip().split())
    graph[x][y] = k
    check[x][y] = True

print(graph)