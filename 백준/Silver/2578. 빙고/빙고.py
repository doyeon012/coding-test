import sys

input = sys.stdin.readline


c = [list(map(int, input().split())) for _ in range(5)]


# mc가 부르는 숫자 저장.
mc = []
for _ in range(5):
  mc += list(map(int, input().split()))
  
  

def check():
  bingo = 0
  
  # 가로 검사(행 기준으로 끊어서 0이 5개인지 확인)
  for x in c:
    if x.count(0) == 5:
      bingo += 1
  
  # 세로 검사(i가 열, j가 행인데 열은 고정시키고 행을 움직여가며 y로 체크해서 0이 5개인지 확인)
  for i in range(5):
    y = 0
    
    for j in range(5):
      if c[j][i] == 0:
        y += 1
    
    if y == 5:
      bingo += 1
  
  # 왼쪽 위 오른쪽 아래 대각선(행과 열이 같으므로)
  d1 = 0
  for i in range(5):
    if c[i][i] == 0:
      d1 += 1
  
  if d1 == 5:
    bingo += 1
  
  # 왼쪽 아래 오른쪽 위 대각선(행, 열이 서로 역순)
  d2 = 0
  for i in range(5):
    if c[i][4-i] == 0:
      d2 += 1
  
  if d2 == 5:
    bingo += 1

  return bingo
    
cnt = 0

for i in range(25):
  
  for x in range(5):
    for y in range(5):
      if mc[i] == c[x][y]:
        c[x][y] = 0
        cnt += 1
  
  if cnt >= 3:
    result = check()
    
    if result >= 3:
      print(i + 1)
      break