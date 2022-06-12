def is_prime(n):
    a = [False, False] + [True]*(n-1)
    primes = []
    lst = []
    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    for x in primes:
        for y in primes:
            if x + y == n:
                lst.append([x,y])
    min = n
    minx, miny =0, 0
    for x,y in lst:
        if abs(x-y) < min:
            min = abs(x-y)
            minx,miny = x, y 
    
    return minx,miny

test = int(input())
for i in range(test):
    even = int(input())
    print(*is_prime(even))