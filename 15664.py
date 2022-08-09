from sys import stdin
from itertools import combinations

n, m = map(int, input().split())
lst = []
lst.extend(list(map(int, stdin.readline().rstrip().split())))
lst.sort()

comb_list = list(combinations(lst, m))
res_lst = []

for x in comb_list:
    if x not in res_lst:
        res_lst.append(x)
    
for x in res_lst:
    print(*x)