n = int(input())

for _ in range(n):
    x = int(input())
    test = []
    flag = 1
    for _ in range(x):
        test.append(input())

    test.sort()
    
    for i in range(x-1):
        if test[i+1].startswith(test[i]):
            flag = 0
            break
    print("NO" if flag == 0 else 'YES')