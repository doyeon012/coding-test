from collections import deque

def solution(n, wires):
    res = 0
    
    # 그래프 초기화 : 각 노드에 대한 빈 리스트 생성
    graph = [[] for _ in range(n+1)]
    
    # 입력받은 wires를 이용해 그래프 구성
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start):
        
        # BFS를 이용해 연결된 노드의 수를 계산하는 함수
        visited = [0] * (n+1)
        q = deque([start])
        visited[start] = 1
        cnt = 1
        
        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
                    cnt += 1
        
        return cnt
    
    # 결과값 초기화: 가능한 최대 차이
    res = n
    
    for a, b in wires:
        # 각 전선을 하나씩 끊어보며 차이 계산
        
        # 그래프에서 해당 간선 제거
        graph[a].remove(b)
        graph[b].remove(a)
        
        # 두 부분으로 나눠진 트리의 노드 수 차이 계산
        res = min(abs(bfs(a) - bfs(b)), res)
        
        # 그래프에 간선 다시 추가 (원상복구)
        graph[a].append(b)
        graph[b].append(a)
    
    return res

n = 9
wries = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wries))