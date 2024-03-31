# 연결 요소의 개수
from collections import deque
import sys
sys.setrecursionlimit(10**6)

#입력 받고, graph 영역을 임의로 2차원 배열을 선언한다.
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

#그래프 형식으로 간선들을 연결해준다. 간선들의 인접 정점들이 저장된다.
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
count = 0
visited = [False] * (n + 1)

#dfs로 구현
def dfs(graph, v, visited):
    visited[v] = True 
    
    # 해당 정점에 append로 들어간 인접 정점을 호출합니다. 
    for i in graph[v]:
        if not visited[i]: # 이미 방문 했으면 넘어가요
            dfs(graph, i, visited) #방문 안했으면 재귀로 호출해요.

#bfs로 구현
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 1번 ~ n번 노드를 순차적으로 방문
for i in range(1, n + 1):
    if not visited[i]: # 방문 안했다는 가정하에 n번 노드와 연결된 모든 노드방문
        bfs(graph, i, visited) # 인접 정점들을 다 재귀로 돌고 최종 끝났을때? 끝나면 count + 1
        count += 1
        
print(count)
               