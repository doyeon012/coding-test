N = int(input())


DP = [0] * (N + 1)
if N >= 1:
  DP [1] = 1
if N >= 2:
  DP[2] = 2
if N >= 3:
  DP[3] = 3


for i in range(4, N + 1):
  DP[i] = DP[i - 1] + DP[i - 2]
  
  
result = DP[N] % 10007
print(result)