from sys import stdin
INF = float("inf") 

# 1
def Bell(start): 
    for i in range(1,n+1):
        for j in range(1, n+1):
            if check[i][j] == True:
                BellmanFord[start][j] = min(BellmanFord[start][j], BellmanFord[start-1][i] + graph[i][j])

# start = 2, i=2, j = 3
# BellmanFord[2][3] = BellmanFord[1][3] 이므로 일단은 3임.
# BellmanFord[2][3] 은 1에서  간선 2개를 사용하여 3까지 가는 것을 의미하므로 Bellman[2][3] = min(간선 하나로 갈 수 있었던 거리(최소), 두개를 사용)
n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)] #값 저장 그래프
BellmanFord = [[INF] * (n+1) for _ in range(n+1)] #1에서 최단거리를 구하기 위한 그래프
check = [[False] * (n+1) for _ in range(n+1)] 

for _ in range(m):
    x,y,k = map(int, stdin.readline().rstrip().split())
    graph[x][y] = k
    check[x][y] = True

BellmanFord[0] = [0] + [INF] * n # 시작 정점 0 으로 초기화
BellmanFord[1] = graph[1] # 간선 하나

# print(BellmanFord)
# print(graph)

for i in range(2,n+1): #n만큼만 돌려보면 확인 가능
    BellmanFord[i] = BellmanFord[i-1][:]
    Bell(i)
    

for idx, value in enumerate(BellmanFord[-1]) :
    #무한으로 돈다
    if idx == 0:
      
        continue
    elif idx == 1:
        if value < 0: 
            print("-1")
            break
    else :
        if value <= 0 or value == INF:
            print("-1")
        else:
            print(value)
print(BellmanFord)