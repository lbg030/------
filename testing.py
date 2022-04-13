sorting = {}
n = input()
li = list(map(int, input().split()))

for i, x in enumerate(sorted(li)):
    # sorting[sorted(li)[i]] = x
    print(i, x)

print(sorting)
