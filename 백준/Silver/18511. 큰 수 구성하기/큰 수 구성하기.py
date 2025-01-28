from itertools import product

N, K = map(int, input().split())
arr = list(map(str, input().split()))
length = len(str(N))

while 1:
  temp = list(product(arr, repeat=length))
  
  answer = []
  
  for i in temp:
    num = int(''.join(i))
    
    if num <= N:
      answer.append(num)
  
  if len(answer) >= 1:
    print(max(answer))
    break
  
  else:
    length -= 1