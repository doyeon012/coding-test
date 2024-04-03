import sys
from collections import deque

input = sys.stdin.readline

# 제품의 개수 입력
n = int(input())

# 각 부품 번호에 따라 다른 부품을 만드는데 필요한 부품 번호와 그 개수 저장
connect = [[] for _ in range(n + 1)]

# 각 제품을 만들 때 필요한 부품의 개수 저장
# ex) needs[A][B]: A를 만드는데 필요한 B의 개수
needs = [[0] * (n + 1) for _ in range(n + 1)]

# 진입 차수 배열: 해당 부품을 만드는데 필요한 다른 부품의 수
degree = [0] * (n + 1)

# 큐 초기화
q = deque()

# 조립 과정 입력 받기
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    # b를 만드는데 a가 c개 필요
    connect[b].append((a, c))
    degree[a] += 1

# 진입 차수가 0인 부품(기본 부품)을 큐에 넣기
for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

# 위상 정렬 시작
while q:
    now = q.popleft()

    # 현재 부품을 사용하여 만들 수 있는 다음 단계 부품 처리
    for next, next_need in connect[now]:
        
        # 현재 부품이 기본 부품(다른 부품 만드는데 사용x)인 경우
        if needs[now].count(0) == n + 1:
            needs[next][now] += next_need
        
        # 현재 부품이 중간 부품인 경우
        else:
            for i in range(1, n + 1):
                needs[next][i] += needs[now][i] * next_need
        
        # 진입 차수 감소 후, 진입 차수가 0이 되면 큐에 추가
        degree[next] -= 1
        if degree[next] == 0:
            q.append(next)

# 마지막 행(최종 제품)을 만드는데 필요한 기본 부품의 개수 출력
for i in range(1, n + 1):
    if needs[n][i] > 0:
        print(i, needs[n][i])
