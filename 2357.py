from sys import stdin

n, m = map(int, input().split())
numberlist = []
#[75, 30, 100, 38, 50, 51, 52, 20, 81, 5]

for i in range(n):
    numberlist.append(int(stdin.readline().rstrip()))

# print(numberlist)
for j in range(m):
    x, y = map(int, input().split())
    maximum = 0
    minimum = numberlist[0]
    for k in range(x-1, y):
        if numberlist[k] < minimum:
            minimum = numberlist[k]
        if(numberlist[k] > maximum):
            maximum = numberlist[k]
    print(minimum, maximum)
