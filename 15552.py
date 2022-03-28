from sys import stdin
n = int(input())
m = []
for _ in range(n):

    m.append(list(map(int, stdin.readline().rstrip().split())))

for x in m:
    print(sum(x))
