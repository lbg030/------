from collections import deque

#음이 다른 경우에도 제거할 필요없이 눌러놓는 상태
n, m = map(int, input().split())

lst = deque(list(map(int, input().split())) for _ in range(n))
finger = [[False] * (m+1) for _ in range(n+1)]
cnt = 0 


# #2차원 리스트로 접근

# #lst를 popleft()해가면서 다 사라질때까지 while문 돌리기
# #전체를 방문해가면서 T/F를 검사하지말고 그 음에 대해서만 for문 돌리기
# while lst:
#     pitch, flat = lst.popleft() # [2,8] 이런 형태로 출력
    
#     #flat - 1까지 체크하는 이유는 flat자체가 눌려있을 수도 있기 때문에 고려해야함.
#     for i in range(m, flat-1, -1): 
        
#         if i == flat:
#             if finger[pitch][flat] == True:
#                 continue
#             else :
#                 finger[pitch][flat] = True
#                 cnt += 1
#                 # print(cnt, pitch,flat, "case 2")
#                 continue
       
#         #case 1 : pitch의 flat보다 높은 flat이 존재 할 때에는 False로 바꿔주고 cnt++
#         if finger[pitch][i] == True:
#             finger[pitch][i] = False
#             cnt += 1
#             # print(cnt, pitch,flat, "case1")
        
#         #case 2 : flat이 존재하지 않을 경우에는 cnt++ && True로 변환
# print(cnt)