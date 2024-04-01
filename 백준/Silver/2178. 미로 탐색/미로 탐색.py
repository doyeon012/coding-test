import sys
from collections import deque

#입력
n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0] #위 - x-1, y 아래 - x+1, y, 왼 - x, y-1, 오 - x, y+1
dy = [0, 0, -1, 1]

def bfs(x, y):
    
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):#상하좌우로 이동하기 때문에
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1: #이동한 nx, ny가 그래프를 벗어남 유무, 1이 있는지
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1 #각 지점의 거리 업데이트
    
    return graph[n-1][m-1] # 최종 끝난의 값 리턴
           
               
                                         
print(bfs(0,0))



