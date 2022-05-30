from itertools import combinations_with_replacement

n,m = map(int , input().split())

li = [i for i in range(1,n+1)]

lst = combinations_with_replacement(li, m)
# if m == 1:
#     for x in li :
#         print(x)
# else :
for x in lst :
    print(*x)