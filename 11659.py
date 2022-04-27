# start, finish 라인 쪽 input().split()으로 하면 시간 초과 남.
# stdin.readline()으로 해도 마찬가지

from sys import stdin
from collections import deque
number, case = map(int, input().split())

lst = list(map(int, input().split()))
for _ in range(case):
    start, finish = map(int, stdin.readline().rstrip().split())
    print(sum(lst[start-1:finish]))
