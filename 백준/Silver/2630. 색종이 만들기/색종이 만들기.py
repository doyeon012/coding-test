# 4분할 정복
# N/2, 맨왼쪽 값 기준으로 전체가 같지 않다면 4개로 분할
# x, y, n//2 - 1사분면, x, y+n//2, n//2 - 2사분면 절반 된 n값으로 이중 for문
#만약 다 같은 값이라면 중간에 흰, 파 각 카운트

import sys

def origami(x, y, count):
    global white_sum, blue_sum
    first_color = num_list[x][y] #사분면의 맨 왼쪽 위
    
    for i in range(x, x+count): # 받은 count값으로 이중 for문으로 전체 조회
        for j in range(y, y+count):
            if first_color != num_list[i][j]: # 다르다? > 4분할go4
                origami(x, y, count // 2) # 1사분면
                origami(x, y + count//2, count // 2) # 2사분면
                origami(x + count // 2, y, count // 2) # 3사분면
                origami(x + count // 2, y + count // 2, count // 2) # 4사분면
                return
    
    #sum 카운트
    if first_color == 0:
        white_sum += 1
    else:
        blue_sum += 1

if __name__ == '__main__':
    #입력
    count = int(sys.stdin.readline())
    num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(count)] 

    white_sum, blue_sum = 0, 0
    
    #출력               
    origami(0, 0, count)
    print(white_sum, blue_sum, sep='\n')