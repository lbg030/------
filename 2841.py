from collections import deque

#음이 다른 경우에도 제거할 필요없이 눌러놓는 상태
#음 달라지는 점이 처리하기가 어려움 -> 딕셔너리로 트라이
#2차원 배열로 visited처럼 시도했으나 메모리초과

n, m = map(int, input().split())

lst = deque(list(map(int, input().split())) for _ in range(n))
finger = {} 
cnt = 0 

while lst:
    pitch, flat = lst.popleft() # [2,8] 이런 형태로 출력
    pitch = str(pitch) # 딕셔너리로 풀기 위해
    
    #pitch가 dic 안에 존재하지 않음.
    if pitch not in finger:
        cnt += 1
        finger[pitch] = [flat]
    
    else :
        if finger[pitch][-1] >= flat :
            
            while len(finger[pitch]) > 0 and finger[pitch][-1] > flat :
                finger[pitch].pop()
                cnt += 1
                # print(cnt, pitch,flat)
                
            if finger[pitch]:
                if finger[pitch][-1] == flat:
                    # print(cnt, pitch,flat)
                    continue
                
            finger[pitch].append(flat)
            cnt += 1
            # print(cnt, pitch,flat)
            
        else :
            finger[pitch].append(flat)
            cnt += 1
            # print(cnt, pitch,flat)

print(cnt)