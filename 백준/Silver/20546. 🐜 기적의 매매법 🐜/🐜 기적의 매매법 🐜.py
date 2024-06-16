# 기적의 매매법
# 구현

money = int(input()) # 초기 현금
MachineDuck = list(map(int, input().split())) # 1일 ~ 14일까지의 주가

# 준현이
money_bnp = money
count_bnp = 0

# 성민이
money_timing = money
count_timing = 0

# 주식 가격 하나씩 순회
for num, price in enumerate(MachineDuck):
    
    # 준현 - 매일 주가를 확인하여 가진 현금으로 최대하 많은 주식 매수
    count_bnp += (money_bnp // price)
    money_bnp %= price
    
    # 성민 - 현재 주식 가격과 다음 3일간의 주식 가격 확인.
    temp = MachineDuck[num:num+4]
    
    # 주식 가격 리스트가 4일차가 되지 않으면(마지막 날이 가까워지면) 루프 종료
    if len(temp) < 4:
        continue
    
    # 주가가 3일 연속 상승 + 주식이 있을 때 매도
    if temp[0] < temp[1] < temp[2] < temp[3] and count_timing > 0: # 매도
        money_timing += (count_timing * temp[3]) # 보유한 주식을 모두 현재 가격에 팔아서 현금으로 교환
        count_timing = 0 # 모두 팔았으므로 보유한 주식 수 0
        
    # 주가가 3일 연속 하락하면 주식 매수.
    elif temp[0] > temp[1] > temp[2] > temp[3]: # 매수
        count_timing += (money_timing // temp[3]) # 성민이 가진 현금으로 최대한 많은 주식을 현재 가격에 매수
        money_timing %= temp[3] # 주식을 매수한 후 남은 현금 업데이트

# 준현의 최종 자산 계산
answer_bnp = money_bnp + count_bnp * MachineDuck[-1]

# 성민의 최종 자산을 계산
answer_timing = money_timing + count_timing * MachineDuck[-1]

# 두 사람의 자산 비교하여 결과 출력
if answer_bnp < answer_timing:
    print("TIMING")
elif answer_bnp > answer_timing:
    print("BNP")
else:
    print("SAMESAME")
