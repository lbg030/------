n = int(input())
m = int(input())
limit = 1000001 ## 511111에 접근하려고 하는데 0,1,2,3,4 가 broken 이라면  555555 에서 접근해야 되기 때문
res = abs(100 - n)

if m :
    broken = set(input().split())
else :
    broken = set()
    
    
#for else 구문 :
    # for 문에서 break가 걸리지 않았다면 else문 으로 이동
for i in range(limit):
    for x in str(i):
        if x in broken:
            break
    else :
        print(i)
        res = min(res, len(str(i)) + abs(i - n))
        
print(res)