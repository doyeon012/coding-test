N = int(input())

num_list = list(map(int, input().split()))

DP = [0] * N

DP[0] = 1

for i in range(1, N):
    max_ = 0
    
    for j in range(i):
        if num_list[j] < num_list[i] and DP[j] > max_:
            max_ = DP[j]
    
    DP[i] = max_ + 1
        
print(max(DP))

