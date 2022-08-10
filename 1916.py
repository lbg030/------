import heapq
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

n = int(input())
m = int(input())
distance = [INF]*(n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
  # a번노드에서 b번 노드로 가는 비용c
  a,b,c = map(int, input().split())
  graph[a].append((b,c))
  
def dijkstra(start):
    q=[]
  # 시작 노드
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
    # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

    # 이미 처리된 노드였다면 무시
    # 별도의 visited 테이블이 필요없이, 최단거리테이블을 이용해 방문여부 확인
        if distance[now] < dist:
            continue
    # 선택된 노드와 인접한 노드를 확인
        for i in graph[now]:
            cost = dist + i[1]
        # 선택된 노드를 거쳐서 이동하는 것이 더 빠른 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
                
start,end= map(int, input().split())

dijkstra(start)

print(distance[end])