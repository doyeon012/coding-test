N = int(input())

dic = {}


for i in range(N):
  _, extension = input().split('.') # .으로 분리
  
  if extension in dic: # 이미 있으면 카운트 +1
    dic[extension] += 1
  else:
    dic[extension] = 1


for key in sorted(dic.keys()): # dic에 있는 키 값들 가져오기, 오름차순은 기본값
  print(key, dic[key])
    