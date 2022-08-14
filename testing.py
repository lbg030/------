import sys
import bisect
#이분탐색으로 최대한 0을 만들수있는 index들 계산
n = int(input())
l1 = list(map(int,sys.stdin.readline().split()))
l1.sort()

def find_key(data):
  return data[3]

def find(arr, target):
  a = 0
  b = len(arr)-1
  ans1 = arr[a]
  ans2 = arr[b]
  while a<b:
    if abs(target-arr[a]-arr[b])<abs(target-ans1-ans2):
      ans1 = arr[a]
      ans2 = arr[b]
    if arr[a]+arr[b]>target:
      b = b-1
    elif arr[a]+arr[b]<target:
      a = a+1
    else:
      return (arr[a],arr[b])
    if a == b:
      continue
  return (ans1,ans2)

res = []
for k in l1:
  #이제 두개의 합이 (-k)가 되도록 투포인터로 탐색을하는거임
  c,d = find(l1,(-k))
  if k == c or k == d or c==d:
    continue
  res.append((k,c,d,abs(k+c+d)))
res = sorted(res,key=find_key)
answer = list(res[0])
del answer[-1]
answer.sort()
print(answer[0], answer[1], answer[2])