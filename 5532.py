l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

e = a // c
f = b // d

if e > f:
    if a % c == 0:
        print(l - e)
    else:
        print(l - 1 - e)
else:
    if b % d == 0:
        print(l - f)
    else:
        print(l - 1 - f)