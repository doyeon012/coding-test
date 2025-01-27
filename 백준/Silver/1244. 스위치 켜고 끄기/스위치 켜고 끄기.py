N = int(input())

switch_arr = list(map(int, input().split()))

people_num = int(input())

for _ in range(people_num):
  
  gender, number = map(int, input().split())
  
  if gender == 1:
    for i in range(number - 1, N, number):
      switch_arr[i] = 1 - switch_arr[i]
  
  if gender == 2:
    index = number - 1
    
    switch_arr[index] = 1 - switch_arr[index]
    
    left, right = index - 1, index + 1
    
    while left >= 0 and right < N and switch_arr[left] == switch_arr[right]:
      
      switch_arr[left] = 1 - switch_arr[left]
      switch_arr[right] = 1 - switch_arr[right]
      
      left -= 1
      right += 1
      

for i in range(0, N, 20):
  print(*switch_arr[i:i + 20])