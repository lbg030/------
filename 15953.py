n = int(input())
for _ in range(n):
    cnt = 0
    m, k = map(int, input().split())
    if(m == 0):
        cnt = 0
    elif(m == 1):
        cnt += 5000000
    elif(m < 4):
        cnt += 3000000
    elif(m < 7):
        cnt += 2000000
    elif(m < 11):
        cnt += 500000
    elif(m < 16):
        cnt += 300000
    elif(m < 22):
        cnt += 100000

    if(k == 0):
        cnt = 0
    elif(k == 1):
        cnt += 5120000
    elif(k < 4):
        cnt += 2560000
    elif(k < 8):
        cnt += 1280000
    elif(k < 16):
        cnt += 640000
    elif(k < 32):
        cnt += 320000

    print(cnt)
