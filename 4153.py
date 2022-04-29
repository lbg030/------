while True:
    n = sorted(list(map(int, input().split())))
    if n[-1] == 0 and n[-2] == 0 and n[-3] == 0:
        break
    if n[-1] ** 2 == (n[-3] ** 2) + (n[-2] ** 2):
        print("right")
    else:
        print("wrong")
