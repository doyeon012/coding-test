N = int(input())

result = []

for i in range(N):
    result.append(int(input()))
    
    
count = 0


for i in range(N-1, 0, -1):
    if(result[i] <= result[i-1]):
        count += result[i-1] - (result[i] - 1)
        result[i-1] = result[i] -1

print(count)