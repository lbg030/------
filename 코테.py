numbers = [ 4,1, 1, 2, 2, 3, 3]
k = 1

def binary(start, lst, k):
    end = len(lst) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if lst[mid] == k:
            return 1

        elif lst[mid] < k:
            start = mid + 1
        else :
            end = mid - 1
            
    return 0

def countPairs(numbers, k):
    numbers = sorted(list(set(numbers)))
    cnt = 0
    for i,value in enumerate(numbers):
        cnt += binary(i, numbers, value + k)
    return cnt
    

print(countPairs(numbers, k))