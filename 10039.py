total = 0
for i in range(5):
    n = int(input())
    if (n < 40):
        n = 40
    total += n

print(int(total / 5))
