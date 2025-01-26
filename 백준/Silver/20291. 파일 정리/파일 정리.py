N = int(input())

dic = {}


for i in range(N):
  
  # 확장자를 얻어야 하므로, 분해
  _, extension = input().split('.')
  
  # N번 반복문 돌테니, 기존에 dic[extension]이 있으면 +1, 없으면 1로 초기화
  if extension in dic:
    dic[extension] += 1
  else:
    dic[extension] = 1


# sorted(dic.keys()) 키 값을 오름차순 정렬
for key in sorted(dic.keys()):
  print(key, dic[key])