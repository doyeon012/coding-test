N, M = map(int, input().split())

arr = []

for _ in range(N):
  arr.append(input())
  
cnt = 0
result = ''

for i in range(M): # M은 문자열의 길이임
  count = [0, 0, 0, 0]
  
  # 열 기준으로 가장 많은 숫자 카운터 세기
  for j in range(N): # 문자열의 개수
    if arr[j][i] == 'A': # 그래서 j, i 이렇게 하면 열 기준으로 됌
      count[0] += 1
    elif arr[j][i] == 'C':
      count[1] += 1
    elif arr[j][i] == 'G':
      count[2] += 1
    elif arr[j][i] == 'T':
      count[3] += 1
  # count에 가장 많은 숫자의 인덱스 숫자를 넣으면 그 내부의 알파벳이 나옴
  idx = count.index(max(count))
  
  # 그 전에 0번에 A의 카운트를 인덱스 했기에 0번이면 A가 가장 많이 나왔다는 뜻이므로 result에 하나씩 쌓기
  if idx == 0:
    result += 'A'
  elif idx == 1:
    result += 'C'
  elif idx == 2:
    result += 'G'
  elif idx == 3:
    result += 'T'
  cnt += N - max(count)

print(result)
print(cnt)