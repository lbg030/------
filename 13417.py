from sys import stdin
from collections import deque

n = int(input())
for _ in range(n):
    m = int(input())
    deq = deque()
    li = stdin.readline().rstrip().split()
    print(li)
    deque.append(li[0])
