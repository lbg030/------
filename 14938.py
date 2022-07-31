import heapq
from sys import stdin

INF = int(1e9)
input = stdin.readline


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


n,m,r = map(int, input().split()) # n은 지역 개수, m은 수색 범위, r은 길의 개수
items = [0] + list(map(int, input().split())) # index 맞추려고 0 넣기
graph = [[] for i in range(n+1)]

res = [0] * (n+1)
for _ in range(r):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

for i in range(1,n+1):
    distance = [INF]*(n+1)
    start = i
    dijkstra(start)
    # print(distance)
    for j in range(1, n+1):
        if distance[j] <= m :
            # if i == 2:
                # print(distance[j], items[j])
            res[i] += items[j]
print(max(res))