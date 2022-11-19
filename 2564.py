x,y = map(int,input().split())
lst = []
n = int(input())
for _ in range(n+1):
    position, value = map(int,input().split())
    if position == 1:
        lst.append(y+value)
    elif position == 2:
        lst.append(-value)
    elif position == 3:
        lst.append(y-value)
    else:
        lst.append(-x-y+value)

total = 2*x+2*y
res = 0

for i in range(n):
    val = lst[n] - lst[i] # 동근이 위치 - 상점 위치
    
    if val<0:
        val *= -1
        
    # 최소 단위 더해주기
    if total - val > val:
        res += val
    else:
        res += (total-val)
print(res)