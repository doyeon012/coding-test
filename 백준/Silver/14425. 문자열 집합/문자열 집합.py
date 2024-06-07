# 입력 준비
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set()

# 첫 번째 집합의 문자열 입력 및 저장.
for i in range(N):
    S.add(input())
    
ans = 0

# 두 번째 집합의 문자열 중 첫 번째 집합에 포함된 문자열 개수 세기
for _ in range(M):
    t = input()
    if t in S:
        ans+=1

# 출력
print(ans)