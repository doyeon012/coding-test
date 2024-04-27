#쉬운 계단 수
#DP

count = int(input())

MAX = 100
DIVIDE = 1000000000

#2차원 배열 선언
dp = [[0] * 10 for _ in range(MAX + 1)]

#1일때 세팅
for i in range(1, 10):
    dp[1][i] = 1

#마지막 자리 수 기준
for i in range(2, 100+1):
    for j in range(9+1): #
        
        if j == 0:
            dp[i][j] = dp[i-1][1] % DIVIDE # 0일때 앞자리가 -1이므로, 뒷자리인 1
            
        elif j == 9:
            dp[i][j] = dp[i-1][8] % DIVIDE # 9일때 뒷자리가 10이므로
            
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % DIVIDE #dp에 저장된 그 전의 값의 j기준 앞뒤 값을 더해준다.
                                                            #왜? 계단수라는 것이 인접한 수랑 1차이가 나므로
            
sum = 0
#결과 출력 - 총 경우의 수를 구하기 때문에
for i in range(0, 10):
    sum = (sum + dp[count][i]) % DIVIDE

print(sum % DIVIDE)
    