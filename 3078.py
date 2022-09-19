from collections import deque

n, k = map(int, input().split())

good_friends = 0

lst = [len(input()) for _ in range(n)]
i = 1
compared_list = deque(lst[:k+i])
# print(compared_list)

while compared_list :
    i += 1
    length = (compared_list.popleft())
    good_friends += compared_list.count(length)
    
    if k + i <= n:
        compared_list.append(lst[-1+k+i])
    # print(compared_list)    
print(good_friends)
    
    
    