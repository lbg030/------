n = int(input())
m = int(input())
limit = 1000001
res = abs(100 - n)

if m :
    broken = set(input().split())
else :
    broken = set()
    
for i in range(limit):
    for x in str(i):
        if x in broken:
            break
    else :
        print(i)
        res = min(res, len(str(i)) + abs(i - n))
        
print(res)