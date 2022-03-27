from itertools import permutations
n = list(input())
print(n)

if('0' in n):
    a = list(permutations(n, len(n)))
    a = list(map(int, a))
    print(a)
else:
    print("-1")
