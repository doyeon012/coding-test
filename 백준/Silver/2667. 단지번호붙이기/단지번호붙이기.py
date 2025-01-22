from collections import deque

# 위, 아래, 오른쪽, 왼쪽
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0 # 처음 방문 처리
    count = 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n: # 그래프의 범위를 벗어나면 안되기 때문에
                continue
              
            if graph[nx][ny] == 1: # 방문하지 않았다면 1일 것
                graph[nx][ny] = 0 # 방문시 0
                queue.append((nx, ny))
                count += 1
                
    return count


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

result = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count = bfs(graph, i, j) # 카운트 체크
            result.append(count) # 결과 배열에 넣자.

# 오름차순 정렬이라는 문제에 조건
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])