from sys import stdout, stdin
n = int(input())
li = []
for _ in range(n):
    li.append(int(stdin.readline()))

for x in sorted(li):
    stdout.write(str(x) + '\n')
