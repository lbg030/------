def a(n):
    ans = 0
    for i in range(1, n+1):
        ans += i
    
    return ans % 10

n = int(input())
print(a(n))