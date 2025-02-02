N = int(input())

# 입력 받는데, 1일부터 할거니 0번째 인덱스에 0, 0넣기.
TP = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

# 1일부터 시작할거니 N+2
dp = [0 for _ in range(N+2)]

# 거꾸로 돌기. DP 계산시 그 히우의 최대 이익이 미리 구해져 있어야함.
for i in range(N,0,-1):

    # i일에 상담 할 수 있는거 +했을 때 퇴사일 넘기면 안됌.
    if i + TP[i][0] -1 > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],dp[i+TP[i][0]]+TP[i][1]) # 점화식 상담 안할때 다음날 최대이익 유지, 상담 하면 끝난 이후의 최대이익에다가 오늘의 상담보수
        
print(dp[1])