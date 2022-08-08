# 학생은 항상 같은 색상의 보석을 가짐
n, m = map(int, input().split()) # n =  학생 / m =  색상
lst = []
for _ in range(m):
    lst.append(int(input()))
    
minimum = 1 # 최소값
maximum = max(lst)  # 최대값

while minimum <= maximum:
    mid = (minimum + maximum) // 2
    student = 0
    
    for x in lst : # 보석을 mid개 만큼 분배했을 때 학생 수
        if x % mid > 0 : # 나머지가 존재 하면 나머지 한명은 mid보다 적게 받는 인원이기 때문에 +1
            student += x // mid + 1
        else : # 딱맞춰서 떨어진 것
            student += x // mid
        
    if student > n: # 실제학생보다 많으면 분배하는 보석을 늘려야함
        minimum = mid + 1
        
    else : # 적거나 같으면 분배 보석을 줄여야함.
        maximum = mid - 1
        ans = mid
print(ans)