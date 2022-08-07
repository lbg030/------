import sys
input=sys.stdin.readline

N=input()[:-1]
INF=10**6
List=[0]*len(N)
List[-1]=1
List[0]=int(0<int(N[0])<10)
for i in range(1,len(N)):
    List[i]=(List[i-1]*(0<int(N[i])<10)+List[i-2]*(9<int(N[i-1]+N[i])<27))%INF
print(List[-1])
