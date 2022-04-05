from sys import stdin
n = int(input())
for _ in range(n):
    li = sorted(list(map(int, stdin.readline().rstrip().split())))
    print(li[-3])
    li = []
