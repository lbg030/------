from sys import stdin

n = int(stdin.readline().rstrip())
a = set(map(int, stdin.readline().rstrip().split()))
m = int(stdin.readline().rstrip())
li = list(map(int, stdin.readline().rstrip().split()))

for i in li:
    if(i in a):
        print("1")
    else:
        print("0")
