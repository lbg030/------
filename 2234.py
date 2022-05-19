# 서쪽에 벽이 있을 때는 1을, 
# 북쪽에 벽이 있을 때는 2를, 
# 동쪽에 벽이 있을 때는 4를, 
# 남쪽에 벽이 있을 때는 8을 더한 값이 주어진다.

#이 성에 있는 방의 개수
# 가장 넓은 방의 넓이
# 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
def bitExpression(k):
    return bin(int(k))[2:].zfill(4)
#이진수로 봤을때 이동은 남동북서 순서임
N,M = map(int, input().split())
lst = [list(map(bitExpression, input().split())) for _ in range(M)]
# print(lst)
visit = [[0] * N for _ in range(M)]