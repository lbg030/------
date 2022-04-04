# (i, j)가 두 배열 모두에 포함되지 않으면, Bi,j = 0이다.
# (i, j)가 두 배열 모두에 포함되면, Bi,j = Ai,j + Ai-X,j-Y이다.
# (i, j)가 두 배열 중 하나에 포함되면, Bi,j = Ai,j 또는 Ai-X,j-Y이다.

from sys import stdin
h, w, x, y = map(int, stdin.readline().rstrip().split())
li = [list(map(int, stdin.readline().rstrip().split())) for _ in range(h+x)]
# print(li)

a_list = [[0] * w for _ in range(h)]
define_a_list = [[0] * w for _ in range(h)]
# print(a_list)
# 하나만 겹치는 칸은 1칸 겹침
# 두칸 겹치는 칸은 2로 표시
for i in range(h):
    for j in range(w):
      # a_list
        if i < h and j < w:
            define_a_list[i][j] += 1
        # b_list 겹치는 부분
        if i+x < h and j+y < w:
            define_a_list[i+x][j+y] += 1

        # 여기까지 했었을 때 안겹치고 A와 B가 아닌 곳들은 다 0으로 처리됨

for i in range(h):
    for j in range(w):
      # 만약 숫자가 1이라면 B랑 겹치지 않는 부분
        if(define_a_list[i][j] == 1):
            a_list[i][j] = li[i][j]
        else:
            a_list[i][j] = li[i][j] - a_list[i-x][j-y]

# print(a_list)
for x in a_list:
    print(*x)
