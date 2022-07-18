lst = [list(input().split()) for _ in range(5)]

print([list(map(lambda x: x.upper(), lst[i])) for i in range(5)])
