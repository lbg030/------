from sys import stdin
 ## 거짓말을 못하는 파티에 사람이 있으면 그 사람 포함 거짓말을 못함
 ##union은 set에서만 사용할 수 있는데 두 셋 간의 동일 요소 출력
n, m = map(int ,input().split())
knowTruth = set(map(int, input().split()[1:])) # 0이면 0 / 아니면 x, y 형태

party = []
knowParty = []
cnt = 0 

for _ in range(m):
    party.append(set(map(int, stdin.readline().rstrip().split()[1:])))# 인원은 상관이 없기 때문에 생략해서 append 한다

for _ in range(m):
    for x in party:
        if x & knowTruth:
            
            knowTruth = knowTruth.union(x)
            

for x in party:
    if x & knowTruth:
        continue
    cnt += 1
    
print(cnt)