from collections import deque

n = int(input())
divided = 1000000007
# 0 1 2 3 4
# 1 2 7 22 71

# 7 * 3 + 2 - 1
# 22 * 3 + 7 - 2

lst = deque([1,2,7])

if n >= 3:
    for _ in range(3, n+1):
        lst.append((lst[2] * 3 + lst[1] - lst[0])  % divided)
        lst.popleft()

    print(lst[-1])
else :
    print(lst[n])

    