# 소가 길을 건너는 이유.

# 입력 받기
n = int(input())

# 변수 초기화 
arr = {} # 소의 번호 and 위치 저장할 딕셔너리 arr 선언
count = 0 # 소가 길을 건넌 횟수

for i in range(n):
    
    # 입력 쌍 처리
    a,b = map(int, input().split())
    
    # 딕셔너리 업데이트 or 카운터 증가.
    if a not in arr: #
        arr[a] = b # a(소의 번호)가 arr(딕셔너리) a(키)값과 b(밸류)값을 arr 저장
    
    else:
        if arr[a] != b: # b(소가 움직인 위치) 같은지 판별
            count +=1 # 길을 건넌 것이므로 숫자 카운트
            
            arr[a] = b # 그 값을 다시 딕셔너리에 넣기

# 같은 a에 대해 다른 b값을 갖는 경우의 수 출력.
print(count)