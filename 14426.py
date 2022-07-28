n, m = map(int, input().split())

check = []
cnt = 0

for _ in range(n):
    check.append(input())

for _ in range(m):
    test = input()
    
    for x in check:
        if x.startswith(test):
            cnt += 1
            break
        
print(cnt)