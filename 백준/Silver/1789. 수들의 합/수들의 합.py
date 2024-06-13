# 수들의 합
# 그리디 알고리즘

# 입력
S = int(input())

# 초깃값 세팅
sum = 0
N = 0

i = 1

# 'sum + i'가 'S'를 넘지 않을 때까지 
while sum + i <= S:
    
    # sum에 i추가.
    sum += i
    
    # 2개다 1씩 추가 인데, N은 
    N += 1 # 더해진 개수
    i += 1 # 더 하려고 하는 현재 자연수

print(N)