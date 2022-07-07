from collections import deque

n, m = map(int ,input().split())
maximum = 100001
visited = [False] * maximum 


def bfs(n):
    q = deque()
    q.append((n, 0))
    least = abs(m-n) #가장 적은 cnt를 저장하기 위한 변수 ## 초기 값은 +1씩 했을때로 가정
    
    while q : 
        value, count = q.popleft()
        visited[value] = True
        
        if value == m :
            least = min(least, count)
        
        if 0<= value -1 < maximum and visited[value -1] == False :
            q.append((value -1, count + 1))
            
        if 0<= value + 1 < maximum and visited[value +1] == False:
            q.append((value +1, count + 1))
        
        if 0 <= value * 2 < maximum and visited[value * 2] == False:
            q.append((value * 2, count))
            
    return least
print(bfs(n))