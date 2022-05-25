from collections import deque

testCase = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y, graph):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    
    while queue :
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= length or ny >= width :
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return 
for i in range(testCase):
    width, length, cabbage = map(int, input().split()) #가로, 세로, 배추위치
    
    #한칸 더 추가한 이유는 오른쪽과 아래쪽을 비교할 건데 
    # 그래프의 끝에선 인덱스 에러가 나는 것을 방지하기 위해
    graph = [[0] * (width) for _ in range(length)] # 가로 세로만큼 그래프
    cnt = 0
    #배추 위치 심기
    for i in range(cabbage):
        y, x = map(int , input().split())
        graph[x][y] = 1

    for x in range(length):
        for y in range(width):
            if graph[x][y] == 1:
                bfs(x,y, graph)
                cnt += 1
    print(cnt)
    print(graph)