#사탕게임
#브루드포스

import sys

input = sys.stdin.readline

n = int(input())
c = [list(input()) for _ in range(n)]

#가로 and 세로 확인 함수
def checkCurMaxNum():
    max_cnt = 1 #최댓값(전체)
    
    for i in range(n):
        
        # 가로 확인
        cnt = 1
        for j in range(1, n):
            if c[i][j] == c[i][j-1]: # 같으면 카운트 +1
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
        
        # 세로 확인
        cnt = 1
        for j in range(1, n):
            if c[j][i] == c[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
    return max_cnt

result = 1

# 행
for i in range(n):
    
    # 열
    for j in range(n - 1):
        
        #오른쪽 교환
        if (j + 1 < n) and (c[i][j] != c[i][j + 1]): # 범위에 벗어나지 않았는지 and 바꾸려는 사탕이 같은 종류x
                                                     # 이미 같으면 바꿔도 result값이 변화x
                                                     
            c[i][j], c[i][j + 1] = c[i][j + 1], c[i][j] # 교체
            result = max(result, checkCurMaxNum())# result가 계속 업데이트 되면서
                                                  # 최종적으로 최대 연속 사탕의 수 저장o
            
            c[i][j], c[i][j + 1] = c[i][j + 1], c[i][j] # 원상복구
            
        #아래쪽 교환
        if (i + 1 < n) and c[i][j] != c[i + 1][j]:
            
            c[i][j], c[i + 1][j] = c[i + 1][j], c[i][j] # 교체
            result = max(result, checkCurMaxNum())
            
            c[i][j], c[i + 1][j] = c[i + 1][j], c[i][j] # 원상복구


print(result)
        
        
    