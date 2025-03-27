N = int(input())
tips = [int(input()) for _ in range(N)]

tips.sort(reverse=True)  

total = 0
for i in range(N):
    give = tips[i] - i  
    if give > 0:
        total += give

print(total)