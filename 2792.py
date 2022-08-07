# 학생은 항상 같은 색상의 보석을 가짐
n, m = map(int, input().split()) # n =  학생 / m =  색상
lst = []
for _ in range(m):
    lst.append(int(input()))
    
minimum = 1
maximum = sum(lst)

while minimum <= maximum:
    mid = (minimum + maximum) // 2
    
    if mid == 0 :
        break
    
    student = 0
    
    for x in lst :
        if x % mid > 0 :
            student += x // mid + 1
        else :
            student += x // mid
        
    if student > n:
        minimum = mid + 1
        
    else :
        maximum = mid - 1
        ans = mid

print(ans)