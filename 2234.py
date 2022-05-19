# 서쪽에 벽이 있을 때는 1을, 
# 북쪽에 벽이 있을 때는 2를, 
# 동쪽에 벽이 있을 때는 4를, 
# 남쪽에 벽이 있을 때는 8을 더한 값이 주어진다.

N,M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
print(lst)