import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque()

for i in range(N):
    comm = input().split()
    
    if comm[0] == 'push':
        queue.append(comm[1]) 
    
    elif comm[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft()) # 큐에서 가장 앞에 있는 정수 출력
    
    elif comm[0] == 'size':
        print(len(queue))
    
    elif comm[0] == 'empty':
        if not queue: # queue가 비었을때 1출력 아니면 0 출력
            print(1)
        else:
            print(0)
    
    elif comm[0] == 'front':
        if not queue: # 큐가 애초에 비었으면 -1, queue[0] 이게 가장 앞에 있는 정수 출력
            print(-1)
        else:
            print(queue[0])
    
    else:
        if not queue:
            print(-1)
        else:
            print(queue[-1])    