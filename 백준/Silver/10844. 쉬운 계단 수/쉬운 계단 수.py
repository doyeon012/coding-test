num = 100

#2차원 배열 선언
dp = [[0] * 10 for _ in range(num + 1)]

count = int(input())

#초깃값 세팅
for i in range(1, 10):
    dp[1][i] = 1


for i in range(2, 100+1):
    for j in range(9+1):
        if j == 0:
            dp[i][j] = dp[i-1][1] % 1000000000
        elif j == 9:
            dp[i][j] = dp[i-1][8] % 1000000000
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] % 1000000000
sum = 0
#결과 출력
for i in range(0, 10):
    sum = (sum + dp[count][i]) % 1000000000


print(sum % 1000000000  )
    