from collections import deque



def bfs(a, b):
  
  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]
  
  queue = deque()
  queue.append((a, b))
  
  while queue:
    
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
        queue.append((nx, ny))
        graph[nx][ny] = graph[x][y] + 1
        
  return graph[N - 1][M - 1]


N, M = map(int, input().split())

graph = []

for _ in range(N):
  graph.append(list(map(int, input())))


print(bfs(0, 0))