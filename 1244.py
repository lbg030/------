from sys import stdin

n = int(stdin.readline().rstrip())
li = list(map(int, stdin.readline().rstrip().split()))

personNumber = int(input())
personList = []

for _ in range(personNumber):
    gender, number = map(int, input())
