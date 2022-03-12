n, m = map(int, input().split())
n = [i for i in range(1, n+1)]
li = list(map(int, input().split()))
todo = 0
print(n.index(li[todo]) < (len(n) // 2))
