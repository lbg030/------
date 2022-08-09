# 1. 두 수를  찾고 나머지 하나는 음수쪽 절대값 작은 값 하나와 양수쪽 절대 값 하나 작은 거 ( 실패 )

# 2. 한 수를 고정하고 그 수에 대해 투포인터 작동

from sys import stdin
n = int(input())
lst = list(map(int, stdin.readline().rstrip().split()))
lst.sort()

# 1. 모든 수가 양수일 때
if lst[0] > 0 :
    print(*lst[:3])
    
# 2. 모든 수가 음수 일 때
elif lst[-1] < 0 :
    print(*lst[-3:])

# 3. 양수와 음수가 섞여 있을 때
else:
    x, y, z = 0, 0, 0
    prev = 3 * int(1e9)
    
    for i in range(len(lst)-1):
        l, r = i+1, n-1
            
        while l < r:
            value = lst[i] + lst[l] + lst[r]
            if value == 0:
                break
            
            elif abs(value) < abs(prev):
                prev = value
                x, y, z  = i, l , r
                
        
            if value < 0 :
                l += 1
            else :
                r -= 1

#반례
#----------------------------------------------------------------

# <케이스>

# 6
# -104336608 239510944 997686289 627058077 722156401 -942278495
# <답>

# -942278495 239510944 722156401

# <케이스>

# 7
# 912022275 -968846127 195376182 -212509759 589371385 817446019 -59843192

# <답>

# -968846127 195376182 817446019