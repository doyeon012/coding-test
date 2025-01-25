word_input = input()

stack = []
result = ''
check = False


for word in word_input:
  
  # 괄호 만나면 기존에 쌓였던 뒤집혀야 할 값 뒤집기
  if word == '<':
    check = True
    
    for _ in range(len(stack)):
      result += stack.pop()
  
  # 보통 값들은 여기서 걸려서 스택에 쌓임
  stack.append(word)
  
  # 괄호 끝났기에 False로 바꾸고 ''.join 이용해서 바로 한번에 넣어주고 스택 비우기
  if word == '>':
    check = False
    
    result += ''.join(stack)
    stack = []
  
  # 공백 만났어? 그럼 < 이거 만났을때와 동일하게 스택에 있는 값들 비우기
  # 근데 스택이 비었어? 그럼 끝!
  if word == ' ' and check == False:
    
    for i in range(len(stack)):
      if i == 0:
        stack.pop()
        continue
      result += stack.pop()
      
    result += ' '

# 스택에 잔존하는 값들이 괄호의 경우가 아니기에 pop 이용해서 역으로 result에 넣기
if stack:
    for _ in range(len(stack)):
      result += stack.pop()
      
print(result)