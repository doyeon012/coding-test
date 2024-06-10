# 폴리오미노
# 디그리

board = input()

count = 0
result = ''

# 문자열의  끝에 도달할 때까지 
while count < len(board):
    
    if board[count:count+4] == 'XXXX':
        result += 'AAAA' # 치환
        count += 4
    
    elif board[count:count+2] == 'XX':
        result += 'BB'
        count += 2
    
    elif board[count] == 'X':
        result = -1 # 변환이 불가. -1 결과값에 넣어주고 while문 종료
        break
    
    # '.'인 경우
    else:
        result += board[count] # 그대로 결과에 추가.
        count += 1

print(result)