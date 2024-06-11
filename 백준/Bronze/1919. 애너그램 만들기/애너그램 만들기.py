# 애너그램 만들기
# 문자열

# 입력 받기
A = input()
B = input()

# 알파벳 빈도 리스트 초기화
a_alphabat = [0] * 26
b_alphabat = [0] * 26

# 첫 번째 문자열의 알파벳 빈도 계산
for a in A: 
    ai = ord(a) - 97 # 'a'는 97부터 시작을 하기 때문에 - 0 ~ 25까지 인덱스 값으로 매핑 가능.
    a_alphabat[ai] += 1

# 두 번째 문자열의 알파벳 빈도 계산
for b in B:
    bi = ord(b) - 97
    b_alphabat[bi] += 1

result = 0

# 빈도 차이를 이용해 제거할 문자 수 계산
for i in range(26):
    result += abs(a_alphabat[i] - b_alphabat[i]) # (a-z)에 대해 두 문자열의 빈도 차이를 절대값으로 계산

# 결과 출력
print(result)