def solution(n, times):
    answer = 0
    times.sort()
    
    start = 0
    end = 1000000000 * 1000000000
    
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for x in times:
            temp += mid // x
            
            if temp >= n:
                answer = mid
                end = mid-1
                break
            
        else :  
            start = mid + 1
        
        # print(start, mid, end)
    # answer = start
        
    return answer

n = int(input())
times = list(map(int, input().split()))

print(solution(n, times))