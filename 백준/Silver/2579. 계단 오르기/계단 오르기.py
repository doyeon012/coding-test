import sys

input = sys.stdin.readline
n = int(input())

# 계단 + dp 배열 계단의 개수만큼 초기화
stairs = [0] * 301
dp = [0] * 301

# 계단의 숫자 1층부터 셋팅
for i in range(1, n + 1):
    stairs[i] = int(input())

# 1, 2, 3번째 계단 셋팅
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

# n번째 계단에 오르기 위해서 전칸에서 바로 or 전전칸에서 온 경우를 통해서 올라오는 경우의 수를 4번째 계단부터 저장.

# 전칸에서 올라온 경우 dp[i - 3]  왜 3이냐? n칸에서 3칸 전까지의 계단을 오르기 위해서의 max값이 dp [i - 3]에저장o
# 그리고 전칸 + 현재 마지막 칸 이렇게 해서 한다. 왜? 마지막 칸은 무조건 밟아야 하고 3칸 연속은 안되기 때문에

# 전전칸에서 올라온 경우 dp[i - 2]왜 2냐? 2칸 전까지의 계단을 오르기 위해서 max 값이 dp[n -2]에 저장o
# 그리고 바로 마지막 칸으로 올라오기 때문에 + 현재칸을 더해준다. 왜? 위와 같은 이유

# 즉 2개중에서 max 값을 dp[n] 에 차곡차곡
for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

#dp에 저장된 n번째 값 출력
print(dp[n])