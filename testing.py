from sys import stdin
lst = list(map(int, stdin.readline().rstrip().split(',')))
sum = sum(lst)
mean = round(sum/(len(lst)-1),1)

print(f"합계 {sum} 평균 {mean} ")