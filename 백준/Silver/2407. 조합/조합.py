N, M = map(int, input().split())

DP = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
  DP[i][0] = 1
  limit = min(i, M)
  for m in range(1, limit + 1):
    if m == i:
        DP[i][m] = 1
    else:
        DP[i][m] = DP[i - 1][m - 1] + DP[i - 1][m]
   
print(DP[N][M])  