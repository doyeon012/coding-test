import sys

input = sys.stdin.readline


N = int(input())

result = []

for i in range(N):
  comm = input().split()
  
  if comm[0] == 'push':
    result.append(comm[1])
    
  
  elif comm[0] == 'size':
    print(len(result))
  
  elif comm[0] == 'pop':
    if not result:
      print(-1)
    else:
      print(result.pop())
      
  elif comm[0] == 'empty':
    if not result:
      print(1)
    else:
      print(0)
  
  elif comm[0] == 'top':
    if not result:
      print(-1)
    else:
      print(result[-1])
    
      