n, m = map(int, input().split())
ground = [list(map(int, list(input()))) for _ in range(n)]
# 0,0 출발 n-1, m-1 도착 벽 한번 부술 수 있음

dx = [1,-1,0,0]
dy = [0,0,1,-1]

