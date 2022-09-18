from sys import stdin
n = int(input())
lst = list(map(int, stdin.readline().split()))

start,end = 0, n-1
x,y = start,end
res = 1e9

if lst[end] < 0:
    print(lst[-2], lst[-1])

elif lst[start] > 0 :
    print(lst[0], lst[1])
    
else :
    while start < end :
        minimum = lst[start] + lst[end]
        if abs(minimum) < res:
            
            x,y = start, end
            res = abs(minimum)
        
        if minimum < 0 :
            start += 1
            
        else :
            end -= 1
        
    lst = sorted([lst[x],lst[y]])
    print(*lst)
