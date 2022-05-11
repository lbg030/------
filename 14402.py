from sys import stdin

n = int(input())
dic = {}
count = 0
for _ in range(n):
    name, work = stdin.readline().rstrip().split()

    if name not in dic and work == '+':
        dic[name] = 1
    