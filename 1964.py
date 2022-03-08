from sys import stdin

n = int(stdin.readline())

# n = 5

plus = 2
middle = 5

# 5 7 10 14 19
s = [0 for _ in range(n+1)]
s[0] = 5
s[1] = 7

for i in range(1, n):

  s[i] = s[i-1] + (7 + 3*(i-1))
  # print("s[", i, "] : ", s[i])
  if(s[i] > 45678):
    s[i] = s[i] % 45678

print(s[n-1])