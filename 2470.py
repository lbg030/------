# value 값을 1e9로 하게 되면 lst안에 1e9만 들어왔을 때 계산이 안됨
# 반례
# 4
# 7 6 -2 -1  
from sys import stdin
n = int(input())
lst = list(map(int, stdin.readline().rstrip().split()))
positiveList = [(i, True) for i in lst if i >=  0]
negativeList = [(abs(i), False) for i in lst if i < 0 ]


lst = positiveList + negativeList
lst.sort()
# print(lst)
value = 3*int(1e9) # 무한으로 초기 설정
x, y = 0,0

for i in range(len(lst)-1):
    if lst[i][1] != lst[i+1][1]:
        if abs(lst[i][0] - lst[i+1][0]) < value:
            value = abs(lst[i][0] - lst[i+1][0])
            x,y = lst[i], lst[i+1]
    #부호가 같다면
    else :
        if lst[i][0] + lst[i+1][0] < value:
            value = lst[i][0] + lst[i+1][0]
            x,y = lst[i], lst[i+1]

res = []
# print(res)
for value in (x,y):
    if value[1] == False:
        res.append(-value[0])
    else :
        res.append(value[0])
        
res.sort()
print(*res)
        