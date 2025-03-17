from  collections import deque
N = int(input())

stack = []
  
for j in range(1, N+1):
  stack.append(j)
  
stack = deque(stack)

for k in range(N - 1):
  stack.popleft()
  stack.append(stack.popleft())

print(stack[0])
  