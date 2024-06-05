# DP 적용

T = int(input())

# dp 초기화 (max가 30개 여서)
dp = [[0] * 30 for _ in  range(30)]

# dp를 활용하여 조합(서로 다른 n개 중에 r개를 선택하는 경우의 수)
for i in range(30):
    for j in range(30):
        
        # 서쪽이 1개 일 때 개수는 j를 따른다.
        if i == 1:
            dp[i][j] = j
            
        else:
            # 서 and 동 개수 똑같으면 추가적인 조합x
            if i == j:
                dp[i][j] = 1 
                
            elif i < j:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1] # 점화식

# 입력
for _ in range(T):
    N, M = list(map(int, input().split()))
    
    # 가장 끝에 있는 dp값 출력
    print(dp[N][M])
            
