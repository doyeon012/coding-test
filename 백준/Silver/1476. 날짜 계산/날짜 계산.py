#날짜 계산

result = 0

E, S, M = map(int, input().split())

#초깃값 세팅
e = 0
s = 0
m = 0
year = 0


while(1):
    if (e == E and s == S and m == M): #  
        break
    
    else:
        #e, s, m은 max값이 다르기 때문에 이 3개의 값이 주어진 E, S, M을 맞추기 위해서
        e += 1
        s += 1
        m += 1
        year +=1
        
        if(e == 16): # 지구 max 15
            e = 1
        
        if(s == 29): # 태양 max 28
            s = 1
        
        if(m == 20): # 달 max 19
            m = 1


print(year)