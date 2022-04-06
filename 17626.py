n = int(input())

if(int(n ** 0.5) == n ** 0.5):
    print("1")

for i in range(1, int(n**0.5) + 1):
    if(int((n-i**2)**0.5) == (n-i**2) ** 0.5):
        print("2")
        break
