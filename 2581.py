m = int(input())
n = int(input())

a = [False, False] + [True]*(n-1)
primes = []
rangePrimes = []
for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

for x in primes:
    if (x >= m):
        rangePrimes.append(x)
# print(f"primes = {primes}")
if (len(rangePrimes) >= 1):
    print(sum(rangePrimes))
    print(rangePrimes[0])
else:
    print("-1")
