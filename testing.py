import sys

h, w, l = map(int, sys.stdin.readline().split())
graph = []

for i in range(h):
    temp = list(sys.stdin.readline().strip())
    graph.append(temp)

# target을 구성하는 알파벳의 빈도수 기록
target = list(sys.stdin.readline().strip())
count, count_graph, x_y = dict(), dict(), dict()
for item in target:
    if item not in count:
        count[item] = 0
        count_graph[item] = 0
        x_y[item] = []
    count[item] += 1

# 지도에 등장하는 알파벳의 빈도수 저장
for x in range(h):
    for y in range(w):
        if graph[x][y] in count:
            count_graph[graph[x][y]] += 1
            x_y[graph[x][y]].append((x, y))

# 강화가 가능한 최대 횟수 구하기
appear = float("inf")
for i in count.keys():
    if appear > count_graph[i] // count[i]:
        appear = count_graph[i] // count[i]

x, y, move = 0, 0, 0
ans = ""

# 강화 횟수만큼 반복 이동할 좌표의 차이를 구해서 계산
for i in range(appear):
    for item in target:
        temp_x, temp_y = x_y[item].pop()

        vertical = temp_x - x
        need = "D" if vertical > 0 else "U"
        for _ in range(abs(vertical)):
            ans += need

        horizontal = temp_y - y
        need = "R" if horizontal > 0 else "L"
        for _ in range(abs(horizontal)):
            ans += need

        ans += "P"
        move += abs(vertical) + abs(horizontal) + 1
        x, y = temp_x, temp_y

temp_x, temp_y = h - 1, w - 1
vertical = temp_x - x
for _ in range(abs(vertical)):
    ans += "D"

horizontal = temp_y - y
for _ in range(abs(horizontal)):
    ans += "R"

move += abs(vertical) + abs(horizontal)
print(appear, move)
print(ans)