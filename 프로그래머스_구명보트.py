def solution(people, limit):
    answer = 0
    
    people = sorted(people)
    
    start, end = 0, len(people) - 1
    
    
    while start <= end :
        
        weight = people[end]
        plus = people[start]
        
        if weight + plus <= limit :
            while weight + plus <= limit :
                start += 1
                plus += people[start]
            end -= 1
        else :
            end -= 1  
        
        answer += 1
    return answer

# people = list(map(int, input().split()))
# limit = int(input())

# print(solution(people, limit))