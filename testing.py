from collections import deque
from re import X


N, M = map(int, input().split())
summing = (N * (N+1) // 2)

check_list = [0] + [1] * N
graph = [[0] * (N+1) for _ in range(N+1)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(M):
    x,y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1


def bfs(v):
        discovered = [v]
        queue = deque(v)
        
        while queue:
            x = queue.popleft()
            for w in graph[x]:
                if w not in discovered:
                    discovered.append(w)
                    queue.append(w)
        print(discovered)
        return sum(discovered)
    
for i in range(1,N+1):
    if i == N:
        print("DISCONNECT")
    
    else:
        k = int(input())
        summing -= k
        check_list[k] = 0
        if check_list[i]:
            flag = bfs(i)
            
            if flag == summing:
                print("CONNECT")  
            else:
                print("DISCONNECT")
                
            continue