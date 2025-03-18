from collections import deque


N, M, V = map(int, input().split())

n_list = [[] for _ in range(N + 1)]
arrr = []

for _ in range(M):
  a, b = map(int, input().split())
  n_list[a].append(b)
  n_list[b].append(a)


for nodes in n_list:
  nodes.sort()

arrr = []
visited = [False for _ in range(N + 1)]
def dfs(V):

  visited[V] = True
  arrr.append(V)
  
  for n_node in n_list[V]:
    if not visited[n_node]:
      dfs(n_node)  
      
dfs(V)
print( ' '.join(map(str, arrr)))

visited = [False for _ in range(N + 1)]

def bfs(V):
  result = []
  q = deque([V])
  visited[V] = True
  
  while q:
    node = q.popleft()
    result.append(node)
    
    for n_node in n_list[node]:
      if not visited[n_node]:
        visited[n_node] = True
        q.append(n_node)
  return result


print(' '.join(map(str, bfs(V))))