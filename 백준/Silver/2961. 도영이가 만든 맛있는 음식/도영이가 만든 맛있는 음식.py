import sys, itertools
from itertools import combinations
input = sys.stdin.readline

N = int(input())
sour = []
bitter = []

# 입력
for _ in range(N): # 재료의 개수 만큼
    a, b = map(int, input().split())
    sour.append(a) # 신맛을 sour에 담기
    bitter.append(b) # 쓴맛을 bitter에 담기

minnn = float('inf') # 최솟값 넣어야 하므로 무한대로 시작

for i in range(1, N+1): # 재료를 i개 뽑을 때
    for food in combinations(range(N), i):
      s = 1
      b = 0

      for j in range(i): 
          s *= sour[food[j]]
          b += bitter[food[j]]
            
      if abs(s - b) < minnn: # abs 절대값 계산
          minnn = abs(s - b)

print(minnn)