#위상정렬

import sys
from collections import deque
input = sys.stdin.readline

#입력 
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
inDegree = [0]*(n+1) # 진입차수 저장
ans = []
q = deque()

#간선들 입력 받으며 진입차수 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) #단방향
    inDegree[b] += 1 #ex) 4 > 2. 2번의 진입차수는 1

#초기에 진입차수가 0인 값들 q에 넣는다. 
for i in range(1, n+1):
    if inDegree[i] == 0: # 진입차수가 0인 값들을 큐에 넣는다. 
        q.append(i)

while q:
    #큐에 가장 먼저들어간것부터 빼고 ans에 넣기
    s = q.popleft()
    ans.append(s)
    
    #넣은 값 인접한 정점들 디그리 -1하고 큐에 넣기. 즉 연결된 간선들 제거.
    for adj_s in graph[s]:
        inDegree[adj_s] -= 1
        if inDegree[adj_s] == 0:
            q.append(adj_s)

print(*ans, sep=" ")