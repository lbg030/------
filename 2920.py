from sys import stdin

lst = list(map(int, stdin.readline().rstrip().split()))
b = sorted(lst, reverse=True)

if sorted(lst) == lst :
    print("ascending")
elif b == lst :
    print("descending")
else :
    print("mixed")