from sys import stdin
n = int(input())
m = list(map(int, stdin.readline().split()))

print(min(m), max(m))
