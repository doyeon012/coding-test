n, target = map(int, input().split())

moneys = []
count = 0

for i in range(n):
    moneys.append(int(input()))

for i in reversed(range(n)): #역순으로 가장 큰 동전부터 시작
    
    if target == 0:
        break # 계산 끝났어? 그럼 종료해.
    else:
        count += target // moneys[i] # 1. 타겟값 보다 작아야 몫이 생긴다
                                 # 2. 카운터에 > 타겟을 동전으로 나눈 몫을 더해준다
        target = target % moneys[i]  # 3. 타겟을 방금 몫 계산하고 남은 값을 넣어서 그 다음 반복문o

print(count) # 최종 동전을 n개 사용해서 타겟값을 만들었을 때 타겟값이 0이 된다.








