import sys
input = sys.stdin.readline

def lower_bound(num_list, target):
  start = 0
  end = N - 1

  while start <= end:
    mid = (start + end) // 2
    if num_list[mid] >= target:
      end = mid - 1
    else:
      start = mid + 1
  return start

def upper_bound(num_list, target):
  start = 0
  end = N - 1
  
  while start <= end:
    mid = (start + end) // 2
    
    if num_list[mid] <= target:
      start = mid + 1
    else:
      end = mid - 1
  return start

N, M = map(int, input().split())
line_list = list(map(int, input().split()))
lines = [list(map(int, input().split())) for _ in range(M)]
line_list.sort()

for start, end in lines:
  start_idx = lower_bound(line_list, start)
  end_idx = upper_bound(line_list, end)
  
  print(end_idx - start_idx)
    
    


  
  