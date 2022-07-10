from collections import deque

T=int(1e5)+1
N,K=map(int,input().split()) # 5 8
Visit=[T for _ in' '*T]

D=deque([[N,0]]) # 5 0
Visit[N]=0 #visit[5] 0

while D:
    [num,count]=D.popleft()
    if Visit[num]>count:Visit[num]=count
    if count<Visit[K]:
        if 0<num*2<min(T,K*2) and Visit[num*2]>count:D.append([num*2,count])
        if 0<num and Visit[num-1]>count+1:D.append([num-1,count+1])
        if num<K and Visit[num+1]>count+1:D.append([num+1,count+1])

print(Visit[K])