from collections import deque

### n = 5 , m = 17
n,m = map(int, input().split())
maximum = 100001
dp = [0] * maximum 

def bfs(n):
    queue = deque()
    queue.append(n)
    while queue:
        check = queue.popleft()
        #종료 조건 check가 m이랑 같아 질 때까지 무한 반복
        if check == m:
            print(dp[m])
            break
        
        for i in (check-1, check+1, check * 2):
            if 0 <= i < maximum and dp[i] == 0 :
                # i번째는 현재 check에서 한번만 수행하면 되기 때문에 +1로 처리
                dp[i] = dp[check] + 1 
                queue.append(i)

bfs(n)