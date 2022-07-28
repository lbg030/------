n = int(input())

for _ in range(n):
    x = int(input())
    test = []
    flag = 1
    for _ in range(x):
        test.append(input())
        
    for x in test:
        if not flag :
            break
        else :
            for y in test:
                if x != y and x.startswith(y):
                    flag = 0
                    print('NO')
                    break
    if flag:
        print("YES")
        

# k = '91125426'
# j = '911'

# print(k.startswith(j))