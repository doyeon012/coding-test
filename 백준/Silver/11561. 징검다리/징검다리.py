def max_jump(n):
    left, right = 1, n
    answer = 0
    
    # 이진 탐색을 통해 최대 점프 거리 찾기
    while left <= right:
        mid = (left + right) // 2
        sum_jump = mid * (mid + 1) // 2  # 1부터 mid까지의 합 계산
        
        if sum_jump <= n:
            answer = mid  # 현재 mid를 가능한 최대 점프로 설정
            left = mid + 1  # 더 큰 값 탐색
        else:
            right = mid - 1  # 더 작은 값 탐색
    
    return answer

# 여러 테스트 케이스를 처리하기 위한 입력 처리
t = int(input())
results = []
for _ in range(t):
    n = int(input())
    results.append(max_jump(n))

# 결과 출력
for result in results:
    print(result)
