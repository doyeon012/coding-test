# 듣보잡

# 입력
N, M = map(int, input().split())

# 입력 받은 문자열 > 집합으로 변환
directory1 = {input().strip() for _ in range(N)}
directory2 = {input().strip() for _ in range(M)}

# 교집합 구하기
result = directory1 & directory2

# 결과를 사전 순서로 정렬
result = sorted(result)

# 출력
print(len(result))
for name in result:
    print(name)
    