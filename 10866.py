from collections import deque
from sys import stdin

n = int(input())

dque = deque()

for _ in range(n):
    # print(dque)
    m = stdin.readline().split()
    if(m[0] == 'push_front'):
        dque.appendleft(m[1])
    elif(m[0] == 'push_back'):
        dque.append(m[1])
    elif(m[0] == 'pop_front'):
        if(len(dque) == 0):
            print("-1")
        else:
            a = dque.popleft()
            print(a)
    elif(m[0] == 'pop_back'):
        if(len(dque) == 0):
            print("-1")
        else:
            a = dque.pop()
            print(a)
    elif(m[0] == "size"):
        print(len(dque))
    elif(m[0] == "empty"):
        if(len(dque) == 0):
            print("1")
        else:
            print("0")
    elif(m[0] == "front"):
        if(len(dque) == 0):
            print("-1")
        else:
            print(dque[0])

    elif(m[0] == "back"):
        if(len(dque) == 0):
            print("-1")
        else:
            print(dque[-1])
