data = input()

stack = []
result = ''
check = False # 괄호안의 여부를 체크

for d in data:
  
    # < 이거 만났을때 기존에 쌓였던 뒤집혀야 할 값 뒤집기
    if d == '<':
        check = True
        for _ in range(len(stack)):
            result += stack.pop()

    # <> 이거 이외에 값들은 여기에 걸림.
    stack.append(d)
    
    # <> 내부에 있었던 값 순차적 처리
    if d == '>':
        check = False
        result += ''.join(stack)
        stack = []    
            
            
    # 공백 만났을때 <이거와 같이 쌓였던 뒤집혀야 할 값 뒤집기
    # 그치만 i=0이다? 그럼 끝내야 함.
    if d == ' ' and check == False:
        for i in range(len(stack)):
            if i == 0:
                stack.pop()
                continue
            result += stack.pop()
        result += ' '
        
# 스택에 값이 남아있는 경우는 괄호의 경우가 아니기에 역으로 추가합니다.
if stack:
    for _ in range(len(stack)):
        result += stack.pop()

print(result)