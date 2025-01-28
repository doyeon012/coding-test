from itertools import combinations

N, M = map(int, input().split())

arr = []

for _ in range(M):
  arr.append(tuple(map(int, input().split())))
  
  

prohibited = set(arr)

count = 0 

# combinations 이용해서 3개로 조합 뽑아내고
for comb in combinations(range(1, N + 1), 3):
  
 # 3개뽑아낸거에 또 2개 뽑아내서 not any 이용해서 피해야 할 조합이 a, b, 혹은 b, a다 들어가 있지 않아야! 피했다는 거니?
 if not any((a, b) in prohibited or (b, a) in prohibited for a, b in combinations(comb, 2)):
        count += 1

print(count)  