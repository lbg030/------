a, b, v = map(int, input().split())

n = ((v-b) / (a-b))
print(int(n) if n == int(n) else int(n)+1)
