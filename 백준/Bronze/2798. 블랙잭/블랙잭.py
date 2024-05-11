#블랙잭
#완전 탐색

# 입력
N, M = map(int, input().split())
arr = list(map(int, input().split()))

#각 sum과 최종 출력할 max값
max = 0
sum = 0

# i
for i in range(N):
    for j in range(i + 1, N): # i보다 + 1
        for k in range(j + 1, N): # j보다 + 1
            sum = arr[i] + arr[j] + arr[k] # 계산식
            
            if(sum <= M): # M보다 작으면서
                if(max <= sum): # max보다 크면 업데이트 go
                    max = sum

#최종 업데이트 된 max값
print(max)