n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

for x in sorted(li):
    print(*x)
