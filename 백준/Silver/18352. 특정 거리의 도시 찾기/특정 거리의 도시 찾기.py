import sys
from collections import deque

input = sys.stdin.readline
N, M, K, X = map(int, input().split())
city = [[] for _ in range(N+1)]

for _ in range(M) :
  A, B = map(int, input().split())
  city[A].append(B)

q = deque([X])

visited = [-1] * (N+1) # X 에서 i 까지의 최단 거리
visited[X] = 0 # 자기 자신에 대한 거리는 0

while q :
  node = q.popleft()
  for next in city[node] :
    if visited[next] == -1 : # 아직 방문하지 않은 노드라면
      visited[next] = visited[node] + 1
      q.append(next)

answer = False

for i in range(1, N+1) :
  if visited[i] == K :
    print(i)
    answer = True
    
if not answer :
    print(-1)