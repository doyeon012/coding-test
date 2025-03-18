from collections import deque

N = int(input())
P = int(input())

n_list = [[] for _ in range(N + 1)]


for _ in range(P):
  a, b = map(int, input().split())
  n_list[a].append(b)
  n_list[b].append(a)


def bfs(start):
  deq = deque([start])
  visited[start] = True
  result_count = 0
  
  while deq:
    node = deq.popleft()
    
    for n_node in n_list[node]:
      if not visited[n_node]:
        visited[n_node] = True
        deq.append(n_node)
        result_count += 1
  return result_count
        

visited = [False for _ in range(N + 1)]
print(bfs(1))
