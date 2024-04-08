#행렬 곱셉 순서

import sys
input = sys.stdin.readline
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)] # 각 행렬의 행과 열의 크기를 입력 받아.

dp = [[0]*(n) for _ in range(n)] # dp[시작행렬][끝행렬] = 시작행렬 ~ 끝 행렬까지의 곱셉 연산 횟수의 증가

#작은 범위 먼저 계산하기 위해서 term 활용 
for term in range(1, n): # term - 연속된 행렬의 개수
    for start in range(n): # 첫 행렬 = start, 끝 행렬 = start + term
         if start + term == n:
             break
         
         dp[start][start+term] = int(1e9) # 지금 계산할 첫행렬과 끝행렬
         
         #행렬이 3개 이상일 때 의미 있어지는 로직
         for t in range(start, start+term):
             #작은 행렬들이 계속해서 쌓이게 된다.
             dp[start][start+term] = min(dp[start][start+term],
                                
                                    #왼쪽 묶음 연산 + 오른쪽 묶음 연산 + 왼쪽 묶음 결과 행렬 * 오른쪽 묶음 결과 행렬
                                    (dp[start][t]) + (dp[t+1][start+term]) + (arr[start][0] * arr[t][1] * arr[start+term][1]))
             
print(dp[0][n-1]) # 첫 번째 행렬 ~ 마지막 행렬까지 곱했을 때의 최소 연산횟수가 저장된거 출력