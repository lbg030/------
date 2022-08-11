l1 = list(map(str,input()))
def who_win(graph):
  win = [False,False]
  #가로
  for i in range(3):
    if graph[(i*3)+0] == graph[(i*3)+1] == graph[(i*3)+2]:
      if graph[(i*3)+0] == 'X':
        win[0] = True
      elif graph[(i*3)+0] == 'O':
        win[1] = True
  #세로
  for i in range(3):
    if graph[i] == graph[i +3] == graph[i + 6]:
      if graph[i] == 'X':
        win[0] = True
      elif graph[i] == 'O':
        win[1] = True
  #대각선
  if graph[0] == graph[4] == graph[8]:
    if graph[0] == 'X':
      win[0] = True
    elif graph[0] == 'O':
      win[1] = True
  if graph[2] == graph[4] == graph[6]:
    if graph[2] == 'X':
      win[0] = True
    elif graph[2] == 'O':
      win[1] = True
  return win
while l1[0] !='e':
  x = l1.count('X')
  o = l1.count('O')
  flag = True
  for k in l1:
    if k == '.':
      flag = False
      break
    else:
      continue
  #경우 나눈다
  # . 이있으면 누군가는 이긴거여야함
  res = who_win(l1)
  valid = False
  if not flag:
    #둘다이기면 안됨
    if res[0] == res[1] == True:
      valid = False
    elif res[0] == True:
      if x-o ==1:
        valid = True
    elif res[1] == True:
      if x == o:
        valid = True
  # .이없으면
  else:
    if x-o == 1:
      if res[0] == True and res[1] == False:
        valid = True
      elif res[0]==False and res[1] == False:
        valid = True
  if valid:
    print("valid")
  else:
    print("invalid")
  l1 = list(map(str,input()))