#스택

#push - X 정수X를 스택에 넣는 연산
#pop - 스택에서 가장 위에 있는 정수 빼고 그 수 출력
#size - 스택에 들어있는 정수의 개수 출력
#empty - 스택에 비어있으면 1, 아니면 0을 출력
#top - 스택의 가장 위에 있는 정수 출력ㅡ 만약 없다? -1을 출력한다.
#단순 스택 시각화 구현

import sys
count = int(sys.stdin.readline())

stack=[]

for _ in range(count):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        stack.append(command[1])
        
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
        
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
            
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
        