from collections import deque
t = deque()
lst = []
lst.append((1,2))
lst.append((2,3))

t.append(lst)
k = deque([[]])
print(len(t))
print(len(k))