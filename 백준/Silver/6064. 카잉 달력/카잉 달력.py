import sys

# 최대 공약수
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

# 최소 공배수
def lcm(a, b):
    return m * n / gcd(a, b)

# 입력
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    
    #연도 입력
    m, n, x, y = map(int, sys.stdin.readline().rstrip().split())
    max_year = lcm(m , n)# m, n의 최소 공배수
    answer = x # answer의 값은 x로 표현할 수 있는 해. 즉 x고정
    
    # x부터 시작해서 y를 찾을때까지 m씩 증가시키기
    while answer <= max_year: # m, n의 최소 공배수 만큼 크기 전까지 
        
        if (answer - 1) % n + 1 == y: # x부터 시작해서 y를 찾을 때까지인데. 마지막 해에서 y가 n과 동일시 0이된다.
            break # while문 빠져나와서 answer 업데이트 그만
    
        answer += m # m씩 증가시키기
    
    if answer > max_year: # answer이 최소공배수를 넘겼을 때는 찾지 못한것이다.
        print(-1)
        
    else:
        print(answer) # 그게 아니라면 answer출력