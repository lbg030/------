num = int(input())
li = map(int, input().split())
count = 0
for x in li:
    if(num == x):
        count += 1

print(count)
