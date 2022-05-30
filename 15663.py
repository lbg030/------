from itertools import permutations
from sys import stdin
n, m = map(int, input().split())

lst = sorted(map(int, stdin.readline().rstrip().split()))
li = sorted(set(permutations(lst,m)))

for x in li:
    print(*x)