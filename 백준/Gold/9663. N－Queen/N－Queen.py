# N-Queen
# 재귀, 백트래킹
# 크기가 N*N 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수 출력.

import sys
input = sys.stdin.readline
 
n = int(input())
 
# 퀸이 공격을 받는지 확인 
def attack(x): # x는 행의 위치
    for i in range(x): 
        # 같은 열에 퀸이있거나 대각선에 퀸이 있는 경우
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return True # 공격o
    return False

# 깊이우선 탐색인 dfs를 통해 각 행을 순회하면서 퀸 배치.
def dfs(start): # start - 현재 탐색하고 있는 행
    global cnt
 
    if start == n: # 모든 행에 퀸을 성공적으로 배치 완료
        cnt += 1
    else:
        
        for i in range(n): # [x, i]에 퀸을 놓는다. i는 열의 위치
            row[start] = i
            if not attack(start): # 퀸의 위협을 받지 않는다면 다음 탐색 
                dfs(start + 1)
 
row = [0] * n #각 행에 위치한 퀸의 열 위치를 저장. ex) row[0] = 3 첫번째 행의 네번째 열의 퀸 존재
cnt = 0 # 퀸의 배치 방법의 수 카운트
dfs(0)
 
print(cnt)