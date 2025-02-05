word_input = input()

stack = []
result = ''
check = False

for word in word_input:
  
  # 괄호 만났을때 기존것들은 다 뒤집기
  if word == '<':
    check = True
    
    for _ in range(len(stack)):
      result += stack.pop()
  
  # 추후 <, >, ' ' 빼고 나머지 값들은 뒤집혀야 하므로 스택에 append로 쌓기
  stack.append(word)
  
  # 괄호 끝났으니 그전에 쌓인 값들 뒤집지 않고 .join으로 한번에 넣기
  if word == '>':
    check = False
    result += ''.join(stack)
    stack = [] # 스택 비우기
    
  
  # 공백을 만나고, check가 False일경우(>) 스택에 있는 값 stack.pop으로 뒤집어서 result에 넣어짐
  if word == ' ' and check == False:
    for i in range(len(stack)):
      if i == 0:
        stack.pop()
        continue
      result += stack.pop()
      
    result += ' ' # 공백 추가해줌

# 스택에 남아있는 값들 pop 이용해서 역으로 result에 넣기  
if stack:
  for _ in range(len(stack)):
    result += stack.pop()
    
print(result)
    