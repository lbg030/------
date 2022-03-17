from itertools import permutations

n, m = map(int, input().split())

li = [x for x in range(1, n+1)]

li2 = permutations(li, m)

for x in li2:
    print(*x)
