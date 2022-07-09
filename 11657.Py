from sys import stdin

INF = float("inf") 
def Bell(start):
    for i in range(n+1):
        for j in range(n+1):
            if check[i][j] == True:
                BellmanFord[start][j] = min(BellmanFord[start][j], BellmanFord[start][j] + graph[start][j])

n, m = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)] #값 저장 그래프
BellmanFord = [[0] * (n+1) for _ in range(n+1)] #1에서 최단거리를 구하기 위한 그래프
check = [[False] * (n+1) for _ in range(n+1)] #방문 여부 // 0 으로 체크하면 돼서 필요 없을수도

for _ in range(m):
    x,y,k = map(int, stdin.readline().rstrip().split())
    graph[x][y] = k
    check[x][y] = True # 필요 없을 수도

BellmanFord[0] = graph[1] # 1에서 출발하는 값 (초기값) 설정 

for i in range(1,n+1): #n만큼만 돌려보면 확인 가능
    Bell(i)