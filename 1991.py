from sys import stdin

n = int(input())

tree = {}

for _ in range(n):
    root,left, right = map(str, stdin.readline().strip().split())
    tree[root] = [left,right]
    
# print(tree)
# {'A': ['B', 'C'], 'B': ['D', '.'], 'C': ['E', 'F'], 'E': ['.', '.'], 'F': ['.', 'G'], 'D': ['.', '.'], 'G': ['.', '.']}
def front(start):
    if start != '.':
        print(start, end='')
        front(tree[start][0])
        front(tree[start][1])
        
def middle(start):
    if start != '.':
        middle(tree[start][0])
        print(start, end='')
        middle(tree[start][1])  

def back(start):
    if start != '.':
        back(tree[start][0])
        back(tree[start][1])
        print(start, end='')
        
front('A')
print()
middle('A')
print()
back('A')