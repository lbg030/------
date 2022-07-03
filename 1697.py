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
        
        sec = dp[check] + 1 #이 부분을 밖으로 빼면 잘 됨
        for i in (check * 2,check-1, check+1):
            if 0 <= i < maximum and dp[i] == 0 :
                dp[i] = sec
                queue.append(i)

bfs(n)