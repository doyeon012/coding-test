# 피로도
# 브루드포스

A, B, C, M = map(int, input().split())

time = 0
now_M = 0
result = 0

while time < 24: # 하루 = 24시간
    
    # 현재 피로도(now_M) + 1시간 피로도(A) <= 최대 피로도(M)
    if now_M + A <= M:
        result += B # 일을 더 해도 됌. 
        now_M += A
    else:
        now_M -= C
        if now_M < 0: # 음수 존재x
            now_M = 0
    time += 1

# 최종 일한 값 출력
print(result)