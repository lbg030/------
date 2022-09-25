#매내쳐 알고리즘 O(n)
from collections import deque

s = list(input())
res = 1

# s가 짝수일 때
if len(s) % 2 == 0:
    pointer = 0
    left_s = deque()
    right_s = deque(s[:])
    
    string = (right_s.popleft())
    
    for i in range(min(len(left_s), len(right_s))):
        