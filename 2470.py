from sys import stdin
n = int(input())
lst = list(map(int, stdin.readline().rstrip().split()))

positiveList = [(i, True) for i in lst if i >=  0]
negativeList = [(abs(i), False) for i in lst if i < 0 ]


lst = positiveList + negativeList
lst.sort()
minimum = [lst[0][0], lst[-1][0], int(1e9)]
for i in range(len(lst)-1):
    if lst[i][1] != lst[i+1][1]:
        if abs(lst[i][0] - lst[i+1][0]) < minimum[2]:
            if lst[i][1] == False:
                minimum = [-lst[i][0],lst[i+1][0], abs(lst[i][0] - lst[i+1][0])]
            
            else :
                minimum = [-lst[i+1][0],lst[i][0], abs(lst[i][0] - lst[i+1][0])]
                
# print(minimum)
print(minimum[0], minimum[1])