from itertools import combinations

li = []
for _ in range(9):
    li.append(int(input()))

n = list(combinations(li, 7))

for x in n:
    if(sum(x) == 100):
        li = x
        break

for x in sorted(li):
    print(x)
