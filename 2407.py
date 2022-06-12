from math import factorial

n, m = map(int, input().split())

answer = 1

for i in range(n - m+1, n+1):
    answer = answer * i
    
print(answer // factorial(m))