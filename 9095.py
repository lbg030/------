n = int(input())


def check(m):
    if(m == 1):
        return 1
    elif(m == 2):
        return 2
    elif(m == 3):
        return 4
    else:
        return check(m-3) + check(m-2) + check(m-1)


for _ in range(n):
    m = int(input())
    print(check(m))
