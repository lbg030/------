n = int(input())
lst = list(map(int, input().split()))
damage = [9,3,1]
cnt = 0

while True :
    lst.sort(reverse=True)
    
    if lst[0] <= 0 :
        print(cnt)
        break
    
    cnt += 1
    
    for i in range(3):
        lst[i] -= damage[i]
    
    
    print(lst)