from collections import deque

N = int(input())

stack = []
ans = []
stack = enumerate(map(int, (input().split())))

stack = deque(stack)

while stack:
  idx, paper = stack.popleft()
  ans.append(idx + 1)
  
  if paper > 0:
    stack.rotate(-(paper - 1))
  elif paper < 0:
    stack.rotate(-paper)

print(' '.join(map(str, ans)))