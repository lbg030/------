n = int(input())
m = int(input())
lst = sorted(list(map(int, input().split())))

cnt = 0

#투 포인터
left, right = 0, n-1
while True :
        #최우선적으로 left랑 right가 같아지면 종료
        if(left >= right):
            print(cnt)
            break
        
        #만약 같으면 맞는 수니깐 left만 증가시키고 다음 while문
        if lst[left] + lst[right] == m:
            # print(lst[left], lst[right])
            cnt += 1
            left += 1
            continue

        #만약 더한 값이 m보다 큰 값이면 더 작은수를 찾아야 함으로 right를 한칸 앞으로 당긴다.( sort되어 있기 때문에 가능)
        elif lst[left] + lst[right] > m:
            right = right - 1
        
        #lst[left] + lst[right] < m
        # lst[left]와 어떤 수를 더해도 m이 되는 수가 존재하지 않음.
        else :
            left += 1

