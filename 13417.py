from sys import stdin
from collections import deque

n = int(input())
for _ in range(n):
    m = int(input())
    deq = deque()
    li = stdin.readline().rstrip().split()
    # print(li)
    deq.append(li[0])
    for x in li[1:]:
        if(ord(deq[0]) < ord(x)):
            deq.append(x)
        else:
            deq.appendleft(x)
    print(''.join(deq))
