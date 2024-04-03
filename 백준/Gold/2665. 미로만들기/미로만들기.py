#미로 만들기
#BFS
import sys
import heapq
input = sys.stdin.readline
n = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(n)]

distance = [[float('inf')]*n for _ in range(n)] #변경횟수 무한으로 초기화

dx = [-1,0,1,0] # 위 - x-1, y 아래 - x+1, y, 왼 - x, y-1, 오 - x, y+1
dy = [0,-1,0,1]

#다익스트라
def dijkstra(d,x,y):
    hq = []
    heapq.heappush(hq,(0,x,y))
    distance[x][y] = 0
    
    #큐 없을 때까지 반복
    while hq:
        d,x,y = heapq.heappop(hq) # 최소힙으로 꺼내기 즉 변경횟수가 가장 적은 노드를 빠르게 선택.
        
        # 목적지 도착
        if x == n-1 and y == n-1:
            print(d) 
            break
        
        # 위, 아래, 왼, 오 탐색.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n and distance[nx][ny]> d+1: # 미로 범위 안에 있고 + 기존 변경횟수 보다 지금이 더 작아?
               
                #업데이트 하러 go 즉 기존 변경횟수가 더 작으면 pass
                if graph[nx][ny] == 0: # 검은벽이야? 
                    distance[nx][ny] = d+1 # 변경횟수 +1
                else: # 흰 벽이야?
                    distance[nx][ny] = d # 변화X
                    
                heapq.heappush(hq,(distance[nx][ny],nx,ny)) # hq에 거리, 좌표순으로 넣어줘.
                     
dijkstra(0,0,0)
