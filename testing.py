def isPrime(m,n):
    a = [False,False] + [True]*(n-1)
    primes = []
    for i in range(2,n+1):
        if a[i]:
            if i >= m:
                primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return sum(primes)

n,m = map(int, input().split())

print(isPrime(n,m))