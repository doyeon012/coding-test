
n = int(input())
target_sequence = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1


for num in target_sequence:
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1
        
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        break
    

if len(stack) == 0:
    for op in result:
        print(op)
        
        
    
    