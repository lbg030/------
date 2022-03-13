from collections import deque
n = int(input())
li = deque([i for i in range(1, n+1)])


while (len(li) != 1):
    # print(li)
    li.popleft()
    li.rotate(-1)

print(li.popleft())
