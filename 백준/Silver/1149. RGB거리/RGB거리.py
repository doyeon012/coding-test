#RGB 거리
#DP
import sys

input = sys.stdin.readline

n = int(input().strip())
costs = []

#입력 받기
for _ in range(n):
    r, g, b = map(int, input().strip().split())
    costs.append([r, g, b])

dp = [[0]*3 for _ in range(n) ]

#첫번째 집 비용 초깃값 설정
dp[0][0] = costs[0][0]
dp[0][1] = costs[0][1]
dp[0][2] = costs[0][2]

#전 값이랑만 색이 다르면 된다.
#dp로 최소값을 쌓아왔기 때문에 전의 값 중에서 더 작은값에 현재 costs의 색을 더한다.
for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0] # 빨
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1] # 초
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2] # 파

# 즉 처음에 입력 받은 n값 즉 dp의 끝 인덱스에 최소값이 들어있을것이다.
# 이 최소값들 중에 최소값을 최종적으로 구한다.
result = min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])
print(result)
