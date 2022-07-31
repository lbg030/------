n = int(input())

m = int(input())

for _ in range(m):
    x,y = map(int, input().split())
    n -= x * y
    
    if n == 0 :
        print("Yes")
        break

else :
    print("No")