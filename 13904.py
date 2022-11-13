n = int(input())

homework = [list(map(int, input().split())) for _ in range(n)]

homework = sorted(homework, key= lambda x : x[1], reverse= True)

visit = [False] * (1001)
print(homework)

answer = 0
for x, y in homework:
    
    day = x
    
    while day > 0 and visit[day]:
        
        day -= 1
        print(day, x, y)
        
    if day == 0:
        continue
    
    else :
        visit[day] = True
        answer += y
        
print(answer)