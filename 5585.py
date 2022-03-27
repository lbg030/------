n = 1000 - int(input())
li = [500, 100, 50, 10, 5, 1]
cnt = 0
for x in li:
    if(n >= x):
        cnt += n // x
        n = n % x

print(cnt)
