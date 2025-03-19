cash = int(input())
cash_list = list(map(int, input().split()))

j_cash = cash
j_stack = 0
for i in range(14):
    if cash_list[i] <= j_cash:
        buy = j_cash // cash_list[i]
        j_stack += buy
        j_cash -= buy * cash_list[i]
j_result = j_cash + j_stack * cash_list[-1]


s_cash = cash
s_stock = 0
high_count = 0
low_count = 0
for i in range(1, 14):    
    if cash_list[i] > cash_list[i - 1]:
        high_count += 1
        low_count = 0
    elif cash_list[i] < cash_list[i - 1]:
        low_count += 1
        high_count = 0
    else:
        high_count = 0
        low_count = 0
    
    if high_count >= 3:
        s_cash += s_stock * cash_list[i]
        s_stock = 0
    if low_count >= 3:
        buy = s_cash // cash_list[i]
        s_stock += buy
        s_cash -= buy * cash_list[i]

s_result = s_cash + s_stock * cash_list[-1]


if j_result > s_result:
    print("BNP")
elif j_result < s_result:
    print("TIMING")
else:
    print("SAMESAME")