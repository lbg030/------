# 에라토스 테네스의 체
n = int(input())
check = [False] * 2 + [True] * (n-1)
primes = []
def isprime(n):
    for i in range(2, n+1):
        if check[i]:
            primes.append(i)
            
            for j in range(2*i, n+1, i):
                check[j] = False

    

isprime(n)
print(primes)

print(check)