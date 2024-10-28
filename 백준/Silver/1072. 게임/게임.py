def min_additional_wins(x, y):
    # 현재 승률 계산
    current_win_rate = (y * 100) // x  

    # 목표 승률 달성 불가능한 경우 처리
    if current_win_rate >= 99:
        return -1

    # 이진 탐색 범위
    left, right = 0, x
    answer = -1  # 목표 승률 달성을 위한 최소 추가 승리 횟수 저장

    # 이진 탐색
    while left <= right:
        mid = (left + right) // 2  # 중간값을 추가 승리 횟수로 설정
        new_win_rate = ((y + mid) * 100) // (x + mid)  # 새로운 승률 계산

        # 목표 승률을 달성
        if new_win_rate > current_win_rate:
            answer = mid  # 현재 mid 값을 후보로 저장
            right = mid - 1  # 더 작은 값
        else:
            left = mid + 1  # 더 큰 값

    return answer  # 최소 추가 승리 횟수 반환

x, y = map(int, input().split())
print(min_additional_wins(x, y))
