n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]
li.sort(key=lambda x: x[0])
li.sort(key=lambda x: x[1])

for x in li:
    print(*x)
