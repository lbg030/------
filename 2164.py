from collections import deque

li = deque([i for i in range(1, int(input())+1)])
# print(li)
li.popleft()
while len(li) != 1:
    # print(li)
    a = li.popleft()
    li.append(a)
    li.popleft()
    # temp = li[0]
    # li[-1] = li[0]
    #     if(len(li) == 1):
    #         break
    #     print(li)
    #     del li[0]

    # print(li[0])
print(li.popleft())
