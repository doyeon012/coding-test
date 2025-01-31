from itertools import combinations

N, M = map(int, input().split())

like = []
# 반복문으로 N명의 사람수만큼 append로 리스트 넣어주기
for i in range(N):
  like.append(list(map(int, input().split())))

cnt = 0

for comb in combinations(range(M), 3): # 조합을 먼저 뽑아냄.
  sum = 0
  
  # 사람 인원수대로 돌릴거임
  for i in range(N):
    p = 0
    
    # 뽑아낸 인덱스 3개로 사람 1명한테서 가장 큰 값을 뽑아냄
    for idx in comb:
      p = max(p, like[i][idx])
    sum += p # 그걸 sum에 넣고
  # 인원수대로 다 돌리고서 N사람수만큼 3개의 치킨 최대치가 저장되면 그걸 cnt에 max로 업데이트   
  cnt = max(cnt, sum)
  
print(cnt)