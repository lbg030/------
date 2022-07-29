from sys import stdin
input = stdin.readline

n,m,r = map(int, input().split()) # n은 지역 개수, m은 수색 범위, r은 길의 개수
items = [0] + list(map(int, input().split())) # index 맞추려고 0 넣기
ground = [[0] * (n+1) for _ in range(n+1)] # 그라운드
for _ in range(r):
    x,y,value = map(int, input().split())
    ground[x][y] = ground[y][x] = value

