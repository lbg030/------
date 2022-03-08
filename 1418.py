from sys import stdin

N = int(stdin.readline())
K = int(stdin.readline())

s = [0 for _ in range(N+1)];
for i in range(2, N+1) :
  if(s[i] == 0 ):
    for j in range(i, N+1, i):
      if (j % i == 0 ) :
        s[j] = max(s[j], i)


ans = 0 
for t in s:
  if(t <= K): 
    ans += 1

print(ans-1)
       