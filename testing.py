import random

fd = open('./playlist.txt', 'r', encoding="UTF-8")
lines = fd.readlines()
lines.sort()
# print(lines)
number = random.randint(0, len(lines))
print(lines[number])
print('플레이리스트 곡 수 ☞ ', len(lines))
fd.close()