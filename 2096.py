import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

max_list = lst
min_list = lst

for _ in range(n-1):
    n1,n2,n3 = map(int,input().split())
    
    max_list = [n1 + max(max_list[0], max_list[1]), n2 + max(max_list), n3 + max(max_list[2],max_list[1])]
    min_list = [n1 + min(min_list[0], min_list[1]), n2 + min(min_list), n3 + min(min_list[2],min_list[1])]
    

print(max(max_list), min(min_list))

# print(max_list, (min_list))