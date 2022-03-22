minimum, maximum = map(int, input().split())

a = [False, False] + [True]*(maximum-1)
primes = []

for i in range(2, maximum+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, maximum+1, i):
            a[j] = False

# print(primes)
cnt = 0
for i in range(minimum, maximum+1):
    testing = 0
    for x in primes:

        if(i >= x**2 >= minimum):
            # print(x**2, i)
            if(i % (x**2) == 0):
                # print(i)
                testing = 1
                break
    if(testing == 0):
        cnt += 1
print(cnt)
