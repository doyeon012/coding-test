N = int(input())
budget_list = list(map(int, input().split()))
M = int(input())
result = 0

start = 0
end  = max(budget_list)

while start <= end:
  mid = (start + end) // 2
  total = 0
  
  for budget in budget_list:
    if budget <= mid:
      total += budget
    else:
      total += mid
  
  if total <= M:
    result = mid
    start = mid + 1
  else:
    end = mid - 1  

print(result)