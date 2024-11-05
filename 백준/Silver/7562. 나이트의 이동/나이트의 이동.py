# 나이트의 이동
# bfs

from collections import deque

def bfs(l, start, finish):
    
    directions = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
    
    queue = deque([(start[0], start[1], 0)]) # 큐에 초기 값 넣기(start_x, start_y)
    
    visited = [ [False] * l for _ in range(l)] # 방문 l*l 만큼 초기화
    visited[start[0]][start[1]] = True # 초기 True
    
    # 큐가 빌 때까지 반복문
    while queue: 
        x, y, moves = queue.popleft() # FIFO로 가장 먼저 넣은거 부터 빼기(BFS)
        
        if(x, y) == finish:# 목적지 도달 했을 때
            return moves # 이동한 수치인 moves 
        
        # 8방향 탐색
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            # 범위 안에 있고 + 방문하지 않았을 때
            if (0 <= nx < l) and (0 <= ny < l) and not visited[nx][ny]:
                visited[nx][ny] = True # 방문표시 하고 
                queue.append((nx, ny, moves + 1)) # 큐에 담자.
    return -1
T = int(input())

for i in range(T):
    l = int(input())
    start_x, start_y = map(int, input().split())
    finish_x, finish_y = map(int, input().split())
    
    # 한번에 넘기기 위해서 튜플 사용
    start = (start_x, start_y)    
    finish = (finish_x, finish_y)
    
    result = bfs(l, start, finish)
    
    # 결과값 즉 moves 값 출력
    print(result)
    