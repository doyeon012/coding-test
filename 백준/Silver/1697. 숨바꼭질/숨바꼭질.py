import sys
from collections import deque

def BFS(v):
  q = deque([v])
  
  while q:
    v = q.popleft()
    
    if v == K: # 찾았으니 종료
      return arr[v]
    
    for n in (v -1, v + 1, v * 2): # 걷거나, 순간이동
      if 0 <= n < MAX and not arr[n]:
        arr[n] = arr[v] + 1
        q.append(n)
      
MAX = 100001 # 문제의 점의 범위가 100,000이므로
N, K = map(int, sys.stdin.readline().split())
arr = [0] * MAX # 현재 위치 v에 도달하는 데 걸린 시간 저장함.
print(BFS(N))