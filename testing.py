n = int(input())
li = [list(input()) for _ in range(n)]
str = li[0][-2:]
str2 = li[1][-2:]
print(str == str2)
