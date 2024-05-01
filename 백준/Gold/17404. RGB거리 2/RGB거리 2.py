#RGB 거리2
#DP
import sys
input = sys.stdin.readline

n = int(input().strip())

arr = []
#입력 받기
for _ in range(n):
    r, g, b = map(int, input().strip().split())
    arr.append([r, g, b])

# 초깃값 설정
INF = float('inf')
# 최소비용 저장 
min_cost = INF

# 첫 번째 집을 각각 고정하고 나머지 집 최소비용 계산
for first in range(3):
    
    dp = [[INF] * 3 for _ in range(n)]
    dp[0][first] = arr[0][first]
    
    # 두 번째 집부터 색칠 비용 계산
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]
    
    # 마지막 집이 첫집과 색이 달라야 함        
    for last in range(3):
            if last != first:
                    min_cost = min(min_cost, dp[n-1][last])   
                                     
print(min_cost)