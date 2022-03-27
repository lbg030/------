n, m = map(int, input().split())

six_package = []
one_package = []

for i in range(m):
    six, one = map(int, input().split())
    six_package.append(six)
    one_package.append(one)

six_min = min(six_package)
one_min = min(one_package)

if n <= 6:
    print(min(six_min, one_min*n))

else:
    print(min(min(one_min * n, six_min * (n // 6)+six_min),
          six_min*(n//6) + one_min * (n % 6)))
