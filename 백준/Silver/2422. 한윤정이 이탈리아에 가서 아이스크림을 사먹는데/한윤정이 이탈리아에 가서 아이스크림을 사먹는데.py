from itertools import combinations

N, M = map(int, input().split())

arr = []

for _ in range(M):
  arr.append(tuple(map(int, input().split())))
  
  

prohibited = set(arr)

count = 0 

for comb in combinations(range(1, N + 1), 3):
  
 if not any((a, b) in prohibited or (b, a) in prohibited for a, b in combinations(comb, 2)):
        count += 1

print(count)  