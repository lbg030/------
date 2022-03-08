from sys import stdin #input대신 사용하는 용도, 속도가 더 빠름

for _ in range(3) :  # 3번의 테스트셋을 받음
  N = int(stdin.readline()); #테스트 개수 받아옴
  total = 0; 
  for i in range(N):
    b = int(stdin.readline()); #테스트 값
    total += b
    
  if(total > 0) :
    print("+")
  elif (total < 0) :
    print("-")
  else :
    print("0")