# 공약수
# 수학

# 모듈 임포트(두 수의 최대 공약수, 제곱근)
from math import gcd, sqrt

# 입력 받기
n = int(input())

# 변수 초기화
lst = []

# 2개의 수에 대한 최대 공약수 계산
if n == 2:
    a, b = map(int, input().split())
    gcd_ = gcd(a, b)

# 3개의 수에 대한 최대 공약수 계산
if n == 3:
    a, b, c = map(int, input().split())
    gcd_ = gcd(gcd(a, b), c)

# 최대 공약수의 약수 찾기
for i in range(1, int(sqrt(gcd_)) + 1): # 제곱근의 소수 부분을 버리고 1을 더해 제곱근 까지 포함.
    
    if gcd_ % i == 0:
        lst.append(i) # 'i'는 'gcd_'의 약수.
        
        # 대칭적인 약수 추가. ex) 'i' = 6, 'gcd_' = 36 -> 6을 추가한다. 
        if i**2 != gcd_: # 아닌 경우
            lst.append(gcd_ // i) 

# 약수 리스트 정렬 및 출력
lst.sort()

for num in lst:
    print(num)

