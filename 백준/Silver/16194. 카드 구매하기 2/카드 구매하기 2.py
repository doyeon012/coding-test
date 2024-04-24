#카드 구매하기 2
#DP
import sys
input = sys.stdin.readline

#초기값 세팅
num = int(input())
li = [0] + list(map(int, input().split()))
dp = [False for _ in range(num + 1)]

for i in range(1, num+1):
    for j in range(1, i+1):
        if dp[i] == False:
            dp[i] = li[j] + dp[i-j]
        else:
            dp[i] = min(dp[i], li[j] + dp[i-j])# 총 i값 만큼 돈을 지불할 수 있다. 
            # j를 사용하면 더 사용할 수 있는 값은 i-j이고
            # ex) i가 4라면 1+3, 2+2, 3+1 앞에가 현재 값j 뒤에가 n원으로 살 수 있는 min값
print(dp[num]) # dp에 저장된 끝값 출력.