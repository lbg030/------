#메모리가 적기 때문에 n 크기 만큼의 heap으로 계속 가져가야함
import heapq

n = int(input())

heap = list(map(int, input().split()))

heapq.heapify(heap)

# print(heap)
for _ in range(n-1):
    lst = list(map(int, input().split()))
    
    for x in lst:
        if heap[0] < x:
            heapq.heappop(heap)
            heapq.heappush(heap, x)

print(heap[0])