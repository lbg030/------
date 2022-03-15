from sys import stdin

n, m = map(int, stdin.readline().split())


a = [False, False] + [True]*(m-1)
primes = []

for i in range(2, m+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, m+1, i):
            a[j] = False

for j in range(n):
    if(primes[j] >= n):
        break

for x in primes[j:]:
    print(x)
