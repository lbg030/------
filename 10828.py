
from collections import deque
from sys import stdin

Stack = deque()

for _ in range(int(input())):
    m = stdin.readline().split()
    # print(m)

    if(m[0] == 'push'):
        Stack.append(int(m[1]))

    elif(m[0] == 'pop'):
        if(len(Stack) > 0):
            pop_entry = Stack.pop()
            print(pop_entry)
        else:
            print('-1')
    elif(m[0] == 'top'):
        if(len(Stack) > 0):
            print(Stack[-1])
        else:
            print('-1')

    elif(m[0] == 'empty'):
        if(len(Stack) == 0):
            print('1')
        else:
            print('0')

    elif(m[0] == 'size'):
        print(len(Stack))
