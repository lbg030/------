from sys import stdin

for _ in range(3) : 
  N = int(stdin.readline());
  total = 0;
  for i in range(N):
    b = int(stdin.readline());
    total += b
  if(total > 0) :
    print("+")
  elif (total < 0) :
    print("-")
  else :
    print("0")