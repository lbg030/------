import sys
input=sys.stdin.readline

N=int(input())
K=int('0b'+input()[:-1],2)
Total=0
while K:
    K=K-(K&((~K)+1))
    Total+=1
print(Total)
