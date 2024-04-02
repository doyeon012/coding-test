# 이분 그래프
import sys
sys.setrecursionlimit(10**6)
k = int(input())


def DFS(start, group):
    visited[start] = group  # 현재 정점의 값 저장

    # 인접 정점 탐색
    for v in graph[start]:
        if visited[v] == 0: # 방문하지 않았어? 탐색 ㄱ
              
            
            result = DFS(v, -group) # 인점 정점에 반대 값을 저장하러 ㄱ
            if not result: #결국 재귀돌다보면 이미 같은 집합에 속하면 False가 리턴되겠죠? 그럼 False 리턴
                return False
        else:
            if visited[v] == group:  # 인접정점의 group값이 현재 나의 group와 같다? 그럼 not 크로스 
                return False
    return True


#모든 정점에서 DFS 탐색
for _ in range(k):
    #정점(V), 간선(E)
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    
    #간선들 입력받음
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    #모든 정점에 대해서 DFS 수행
    for i in range(1, V+1):
        if visited[i] == 0:
            
            result = (DFS(i, 1))
            
            if not result: # 인접 노드끼리 다른 집합에 속하지 않으면 False를 반환하는데 그럼 바로 끝내
                break
            
    print("YES") if result else print("NO")