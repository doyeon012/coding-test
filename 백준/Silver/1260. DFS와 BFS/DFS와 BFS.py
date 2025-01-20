from collections import deque

n, m, v = map(int, input().split())
graph = [[False] * (n+1) for _ in range(n+1)] # 임의로 False 넣어줌.

#정점, 간선 입력 받음.
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

#방문 여부 확인    
visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)

def dfs(v):
    visited1[v] = True
    print(v, end=" ")
    
    for i in range(1, n + 1):
        if not visited1[i] and graph[v][i] == 1:
            dfs(i)# 재귀타고 계속 들어가서 탐색o


def bfs(v):
    q = deque([v])
    visited2[v] = True
    
    #새로운 노드가 추가 되지 않고 앞에서 부터 빼고 없으면 끝!
    while q:
        #q 맨 앞에 있는 정점을 popleft()로 꺼내서 print
        v = q.popleft()
        print(v, end=" ")
        
        #그 같은 위치에 있는 친구들 전부 append로 이어 붙여. 이걸 또 popleft로 앞에서 부터 뺄거니
        for i in range(1, n + 1):
            if not visited2[i] and graph[v][i] == 1:
                q.append(i)
                visited2[i] = True

dfs(v)
print()
bfs(v)
        

