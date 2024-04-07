#회의실 배정
#디그리 알고리즘
n = int(input())

time = [[0] * 2 for _ in range(n)] # n개 행에 2개열을 가진 2차원 리스트 생성.

for i in range(n):
    s, e = map(int, input().split())
    time[i][0] = s # 인접리스트
    time[i][1] = e

#끝나는 시간을 기준으로 정렬 - 회의 종료 후 > 다음으로 가장 빨리 끝나는 시간 선택
#즉 가성비 를 따져서 최적의해를 구하자.
time.sort(key = lambda x: (x[1], x[0]))

#첫번째 회의는 필수
count = 1
end_time = time[0][1]

for i in range(1, n):
    if time[i][0] >= end_time:# 시작시간이 끝나는 시간보다 커? > 회의 가능
        end_time = time[i][1] # 종료시간 업데이트
        count +=1
    
print(count)