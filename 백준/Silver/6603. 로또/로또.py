import itertools

# exit() 전까지.
while True:

    array = list(map(int, input().split()))

    k = array[0] # 집합 S에 포함되는 수.
    S = array[1:]

    for i in itertools.combinations(S, 6): # 리스트 'S'에서 6개의 요소를 선택하는 모든 가능한 조합 생성.
        print(*i) # i 요소를 공백으로 구분하여 출력.

    # 첫 번째 숫자가 0이면 더 이상 입력x 프로그램 종료
    if k == 0:
        exit()
        
    print() # 각 테이스 테이스 사이에 빈 줄을 출력.