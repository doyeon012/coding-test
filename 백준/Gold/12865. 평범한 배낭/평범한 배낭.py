#배낭 문제
n, k = map(int, input().split())  # 물건 개수, 배낭 크기
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]  # 배열

item = [[0, 0]]
for i in range(1, n + 1):  # 물건의 무게, 가치 입력
    item.append(list(map(int, input().split())))

Max = 0
#물건 개수, 배낭의 크기 만큼 2중 반복문 돌려서 배열에 값들을 담자.
for i in range(1, n + 1):  # 물건 개수만큼
    for j in range(1, k + 1):  # 배낭의 크기만큼

        weight = item[i][0]
        value = item[i][1]
		# 가방에 넣을 수 없아?
        if j < weight:
            dp[i][j] = dp[i - 1][j]# 그전에 넣었던 값 넣어줘.
            
        # 가방에 넣을 수 있어?
        else: 
            dp[i][j] = max(dp[i - 1][j],value + dp[i - 1][j - weight])
               # 위에 값 vs 
               # (현재 아이템 가치 + 그 전 단계에서 구한 남은 무게(더 담을 수 있는)의 가치max값

print(dp[n][k])# 최종 끝값 출력.