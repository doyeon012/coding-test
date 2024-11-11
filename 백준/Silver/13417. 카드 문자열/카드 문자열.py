from collections import deque


t = int(input())

# 각 테스트 케이스 반복
for _ in range(t):
    n = int(input())
    # 카드를 deque 자료구조로 입력받기
    cards = deque(input().split())

    # 결과를 저장할 문자열
    res = ''
    
    while cards:
        s = cards.popleft()  # 왼쪽에서 카드를 하나 꺼냄

        # 만약 현재 문자열 res가 비어 있으면 첫 번째 카드 추가
        if not res:
            res += s
        else:
            # 현재 카드 s가 res의 첫 번째 문자보다 사전순으로 빠르면 앞에 추가
            if s <= res:
                res = s + res
            # 그렇지 않으면 뒤에 추가
            else:
                res = res + s

    
    print(res)