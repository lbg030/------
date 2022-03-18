from collections import deque

a = deque()
m = "push 1"

a.append([1])
a.append(m)
a.append('a')
a.append('c')
a.append('es')
a.append('b')
a.append('a')
a.append('b')
a.pop()

print(a)
