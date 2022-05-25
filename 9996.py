Case = int(input())
target = list(map(str, input().split('*')))

for i in range(Case):
    #무조건 2개로 나뉘게 되어있음.
    first = len(target[0])
    last = len(target[1])
    compared = input()
    