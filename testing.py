#BFS 및 deque 사용 -> 실패 
import sys
import collections

#값 범위 안에 있는지 check
def is_in_range(H,N,M,h,r,c) :
    return h>=0 and r>=0 and c>=0 and h<H and r<N and c<M

#입력 읽어오기
#visited 배열 생성 및 초기화
M, N, H = map(int, sys.stdin.readline().split())
box = [[sys.stdin.readline().split() for i in range(N)] for j in range(H)]
not_visited = [[[1]*M for _ in range(N)] for _ in range(H)]
number_of_tomato = M*N*H
queue = collections.deque()
ripen = 0
#토마토 익을때 까지 걸리는 시간

direction = ((-1, 0, 0), (1, 0, 0), (0, -1, 0),(0, 1, 0), (0, 0, -1), (0, 0, 1))

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == '1':
                queue.append((i, j, k, 0))
            elif box[i][j][k] == '-1':
                number_of_tomato -= 1

#BFS 수행 , queue에서 토마토 꺼낼 때 마다 토마토 개수 줄이기

while queue:
    h, r, c, ripenn = queue.popleft()
    number_of_tomato -= 1
    for i, j, k in direction:
        nh, nr, nc = h+i, r+j, c+k
        if nh >= 0 and nr >= 0 and nc >= 0 and nh < H and nr < N and nc < M:
            if not_visited[nh][nr][nc] and box[nh][nr][nc] == '0':
                queue.append((nh, nr, nc, ripen+1))
                not_visited[nh][nr][nc] = False

print(ripen if number_of_tomato == 0 else -1)