from itertools import permutations

N = int(input())
K = int(input())

arr = []
for i in range(N):
  arr.append(input())
  
temp = []
card = list(permutations(arr, K ))

for i in card:
  temp.append("".join(i))

result = set(temp)
  
print(len(result))