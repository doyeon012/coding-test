def solution(n, times):
		# 초기 세팅
    left = 1
    right = max(times) * n  # 최악의 경우 가장 느린 심사관만이 모든 사람을 처리하는 경우

    answer = right  # 최소 시간을 최악의 경우로 하고 시작

    # 이분 탐색
    while left <= right:
        mid = (left + right) // 2 # 계속 업데이트 된 값으로 갱신되어서 그래서 이분 탐색

        # 각 심사관이 mid 시간 내에 처리할 수 있는 사람 수의 총합을 계산
        total_people = sum(mid // time for time in times)

        if total_people >= n:  # n명을 처리할 수 있는 경우
            answer = mid  # 갱신
            right = mid - 1  # 왼쪽기준 살리고 오른쪽 없애기 위해
        else:
            left = mid + 1  # 오른쪽 기준 살리고 왼쪽 없애고

    return answer 