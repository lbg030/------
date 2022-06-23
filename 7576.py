from sys import stdin

n,m = map(int, input().split())

lst = [list(map(int, stdin.readline().rstrip().split())) for i in range(m)]

print(lst)