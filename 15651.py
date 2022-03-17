from itertools import product

n, m = map(int, input().split())

for i in product([x for x in range(1, n+1)], repeat=m):
    print(*i)
    # li = []

    # for _ in range(m):
    #     li.append(x for x in range(1, n))

    # for x in li:
    #     print(x)
