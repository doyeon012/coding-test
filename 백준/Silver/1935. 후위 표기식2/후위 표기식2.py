import sys
input = sys.stdin.readline

N = int(input())
equation = input().strip()
num_list = [int(input()) for _ in range(N)]

stack = []
    
for i in equation:
    if 'A' <= i <= 'Z':
        stack.append(num_list[ord(i) - ord('A')])
    # 연산자 만날 경우
    else:
        str2 = stack.pop()
        str1 = stack.pop() # 2개를 꺼내서 연산하고서!
        
        # 다스 스택에 넣어줌.
        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)
print(f'{stack[0]:.2f}')  