# 섬의 개수
# 그래프
# DFS
import sys
sys.setrecursionlimit(10**6)
 
def dfs(x, y, grid, visited):
        
        # 상, 하, 좌, 우, 대각선
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        # 방문처리
        visited[x][y] = True

        # 8방향 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
        
            # 유효한 범위 내에 있고, 방문하지 않았으며, 1인경우
            if  0 <= nx < len(grid)  and  0 <= ny < len(grid[0])  and not visited[nx][ny] and grid[nx][ny] == 1:
                dfs(nx, ny, grid, visited)




while True:
    W, H = map(int, input().split())
    
    # 둘 중에 하나라도 0을 입력 받으면 종료
    if W == 0 and H == 0:
        break
    
    visited = [[False] * W for _ in range(H)]
    grid = [list(map(int, input().split())) for _ in range(H)]
    
    count = 0
    
    # 전체 탐색(grid 유효 범위 안에 있고, 방문하지 않은 경우에 dfs 함수로 들어가기.)
    for i in range(H):
        for j in range(W):
            
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j, grid, visited)
                count += 1
    
    print(count)








