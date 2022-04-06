n, m = map(int, input().split())
dic = {}
for _ in range(n):
    site, password = map(str, input().rstrip().split())
    dic[site] = password

for _ in range(m):
    searchSite = input()
    print(dic[searchSite])
