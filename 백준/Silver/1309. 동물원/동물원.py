#동물원
#dp

count = int(input())

dp = [[0] *3 for _ in range(count + 1)]

dp[1][0] = 1 
dp[1][1] = 1
dp[1][2] = 1

for i in range(2, count + 1 ):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][1] + dp[i-1][0]) % 9901

print((dp[count][0] + dp[count][1] + dp[count][2]) % 9901)

