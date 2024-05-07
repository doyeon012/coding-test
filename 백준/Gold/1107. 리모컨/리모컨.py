#리모컨
#브루드포스

# 입력
target = int(input())
ans = abs(100 - target) # 시작값이 100이므로 절댓값으로 
M = int(input())

# 고장난 버튼 유무에 따라서
if M: 
    broken = set(input().split())
else:
    broken = set()
    
# 큰수 > 작은수 내려올 수 있으니 1,000,000까지 봐야함
for num in range(1000001):
    
    # 고장난 버튼 확인
    for N in str(num):
        if N in broken: 
            break
        
    else:
        # 기존값, num을 문자열로 바꿔서 개수 + 타겟과의 차이(절댓값)
        ans = min(ans, len(str(num)) + abs(num - target))

print(ans)