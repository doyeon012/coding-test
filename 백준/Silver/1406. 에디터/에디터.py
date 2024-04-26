#에디터
#스택
import sys
input = sys.stdin.readline

#입력
stack1 = list(input().strip())
stack2 = []
count = int(input())

for _ in range(count):
    editor = input().split()
    
    #pop 할때 리스트가 있는지 확인(예외 처리)
    if (editor[0] == 'L' and stack1):
        stack2.append(stack1.pop()) # stack1(pop) > stack2(append)
        
    elif editor[0] == 'D' and stack2: 
        stack1.append(stack2.pop()) # stack2(pop) > stack1(append)
        
    elif editor[0] == 'B' and stack1: # 커 왼쪽에서 삭제
        stack1.pop()
        
    elif editor[0] == 'P':
        stack1.append(editor[1]) #뒤에 입력받은 영문 소문자 왼쪽에서 추가

answer = stack1+stack2[::-1]# - pop > append는 뒤에서(뽑고) 앞에서 부터(넣었기) 역순이 되었기 때문에 
print(''.join(answer))

    