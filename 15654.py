from sys import stdin
from itertools import permutations

n, m =map(int, input().split())

lst = sorted(list(map(int, stdin.readline().rstrip().split())))

li = permutations(lst, m)

for x in li :
    print(*x)