# 연결 요소의 개수
from collections import deque
import sys
sys.setrecursionlimit(10**6) # 깊이 제한 방지.

#입력 받고, graph 영역을 임의로 2차원 배열을 선언한다.
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)

#그래프 형식으로 간선들을 연결해준다. 간선들의 인접 정점들이 저장된다.
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

#dfs로 구현
def dfs(v):
    visited[v] = 1
    # 해당 정점에 append로 들어간 인접 정점을 호출합니다. 
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i) #방문 안했으면 재귀로 호출해요.


# #bfs로 구현    
# queue = deque([1])
# while queue:
#     v = queue.popleft()
#     for i in graph[v]:
#         if not visited[i]:
#             queue.append(i)
#             visited[i] = True


dfs(1)        
print(sum(visited)-1) # 1번 컴퓨터 본인은 제외.
#bfs로 할거면 dfs 주석처리하고 bfs 주석 풀면 된다. 동일 메커니즘이어서 가능.