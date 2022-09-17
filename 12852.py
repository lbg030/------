n = int(input())

ans = [n]

while n != 1:
    if (n-1) % 3 == 0:
        n = n - 1
        ans.append(n)
        n //= 3
        ans.append(n)
        
    elif (n-1) % 2 == 0:
        if n % 3 == 0:
            n //= 3
            ans.append(n)
        else :
            n = n - 1
            ans.append(n)
            n //= 2
            ans.append(n)
    
    else :
        n = n - 1
        ans.append(n)

print(len(ans)-1)
print(*ans)
