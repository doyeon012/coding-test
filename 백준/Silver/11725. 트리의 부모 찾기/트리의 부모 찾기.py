import sys
from collections import deque
sys.setrecursionlimit(10**9)

#입력
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 부모 > 자식으로 이동. visited 배열의 index 탐색을 시작한 node = 부모노드 저장. 즉 단순히 0을 저장x, 부모노드 저장.
# dfs로 구현
def dfs(s):
    for nxt in graph[s]:
        if visited[nxt] == 0:
            visited[nxt] = s
            dfs(nxt)
one = 1
#큐에서 n을 꺼내고 n의 자식들 탐색 > 탐색하는 과정에서 단순히 visited를 방문 체크x, 자식들 저장공간에 n을 넣어줌.               
#bfs로 구현
queue = deque([one])
def bfs():
    while queue:
        s = queue.popleft()
        
        for nxt in graph[s]: 
            if visited[nxt] == 0: 
                visited[nxt] = s
                queue.append(nxt)
                             
# dfs(one)                
bfs()

for i in range(2, n+1):
    print(visited[i])
    

