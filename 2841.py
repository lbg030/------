from collections import deque

#음이 다른 경우에도 제거할 필요없이 눌러놓는 상태
n, m = map(int, input().split())

lst = deque(list(map(int, input().split())) for _ in range(n))
flat = []
cnt = 0 

