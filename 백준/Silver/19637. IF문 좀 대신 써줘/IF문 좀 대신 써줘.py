import sys
input = sys.stdin.readline

N, M = map(int, input().split())
title_list = []
for i in range(N):
  title, power = input().split()
  power = int(power)
  title_list.append((title, power))
character_list = [int(input()) for _ in range(M)]

result_list = []

for character in character_list:
  start = 0
  end = N - 1
  
  while start <= end:
    mid = (start + end) // 2
    if character <= title_list[mid][1]:
      end = mid - 1
    else:
      start = mid + 1
  
  result_list.append(title_list[start][0])

print('\n'.join(result_list))
  
    
  
  