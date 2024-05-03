#합분해
#DP[]

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0] * (N + 1) for _ in range(K + 1)]

#초깃값 설정
dp[0][0] = 1


# 사용할 수 있는 정수의 개수(K)
for k in range(1, K + 1):
    
    # 만들어야 할 정수(N)
    for n in range(N + 1):
        if n > 0 :
            dp[k][n] = (dp[k-1][n] + dp[k][n-1]) % 1000000000 # 사용할 수 있는 정수의 개수K-1을 0~n dp로 쌓는다.
        else:
            dp[k][n] = dp[k-1][n]
    
print(dp[K][N])

        