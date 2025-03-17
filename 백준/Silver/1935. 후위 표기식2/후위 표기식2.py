import sys
input = sys.stdin.readline

N = int(input())

equation = input().strip()
num_list = [int(input()) for _ in range(N)]

stack = []

for i in equation:
  if 'A' <= i <= 'Z':
    stack.append(num_list[ord(i) - ord('A')])
  
  else:
    str2 = stack.pop()
    str1 = stack.pop()
    
    if i == '+':
      stack.append(str1 + str2)
    elif i == '-':
      stack.append(str1 - str2)
    elif i == '*':
      stack.append(str1 * str2)
    elif i == '/':
      stack.append(str1 / str2)

print(f'{stack[0]:.2f}')