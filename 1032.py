from sys import stdin

N = int(stdin.readline())

li = []
sen = ""
count = 0

for t in range(N):
  b = stdin.readline()
  li.append(b)

# # print(li)
# # print(len(li[0]))
# # print(len(li[1]))
# print(li[0])
# print(li[1])
# # print(li[0][11])
# # print(li[0][1] == li[1][1]) #True
# print(len(li[-1]))

for j in range(len(li[-1])):
  for k in range(len(li)):
    if(li[k][j] == li[k-1][j]):
      count += 1
  if(count == N ) :
    sen += li[k][j]
  else :
    sen += "?"

  count = 0
print(sen)
