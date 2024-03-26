#스택
# 탑
# 포인트 - 현재 탑의 높이가 전에 넣은 스택의 탑을 지워서 굳이? 끝까지 안가도 된다. 
# 포인트 - 전에 넣은 스택의 탑크기가 더 크다? 그럼 전에 넣은 스택의 인덱스 +1 해서 넣어줌.
import sys
count = int(sys.stdin.readline())
top_list = list(map(int, sys.stdin.readline().split()))
stack = []
answer = []

for i in range(count):
    
    while stack:
        
        # 그 전의 탑크기가 더 커>? 그 전의 탑 인덱스를 +1해서 넣어주기. 
        # 작아? 그럼 스택에서 마지막 값 삭제
        if stack[-1][1] > top_list[i]: 
            answer.append(stack[-1][0] + 1) 
            break
        else:
            stack.pop()
            
    if not stack: # 스택이 비어? 레이저를 수신할 탑이 없다.
        answer.append(0) 
        
    stack.append([i, top_list[i]]) # 스택에 인덱스랑 값을 넣어준다.


# answer을 문자열로 변환하고 join으로 스페이스바 한번에 출력한다.
print(" ".join(map(str, answer)))


