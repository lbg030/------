from collections import deque
n = int(input())
fibonacci = deque([0,1])

for _ in range(2,n+1):
    number = fibonacci[-2] + fibonacci[-1]
    if number > 1000000007:
        number = number % 1000000007
    fibonacci.append( number)
    fibonacci.popleft()
print(fibonacci[-1])