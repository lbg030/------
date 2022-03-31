n = 250000
a = [False, False] + [True]*(n-1)
primes = []

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
# n = 2
# print(a[n:])
# print(primes)
while True:
    count = 0
    t = int(input())
    if(t == 0):
        break
    for i in range(t+1, 2*t+1):
        if a[i] == True:
            # if(t == 13):
            # print(f"i={i}")
            count += 1
    print(count)
