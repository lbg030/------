# start, finish 라인 쪽 input().split()으로 하면 시간 초과 남.

from sys import stdin

number, case = map(int, input().split())

lst = list(map(int, input().split()))
for _ in range(case):
    start, finish = map(int, stdin.readline().rstrip().split())
    print(sum(lst[start-1:finish]))
