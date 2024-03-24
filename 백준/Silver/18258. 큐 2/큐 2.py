#큐2

# push X: 정수 X를 큐에 넣음
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수 출력.
# empty: 큐가 비어있으면 1, 아니면 0을 출력.
# front: 큐의 가장 앞에 있는 정수를 출력. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 시간복잡도가 O(1)로 이뤄져야 시간 초과x > 그렇기 때문에 deque 사용
import sys
from collections import deque

count = int(sys.stdin.readline())
queue = deque()

for i in range(count):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        queue.append(command[1])

    elif command[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft()) # 가장 먼저 들어간 것 제거
    
    elif command[0] == "size":
        print(len(queue))

    elif(command[0] == "empty"):
        if not queue:
            print(1)
        else:
            print(0)
    
    elif(command[0] == "front"):
        if not queue:
            print(-1)
        else:
            print(queue[0])
    
    else:
        if not queue:
            print(-1)
        else:
            print(queue[-1])
        