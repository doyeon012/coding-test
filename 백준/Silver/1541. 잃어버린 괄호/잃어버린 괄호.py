#잃어버린 괄호 

# - 기준으로 숫자들을 나눈다.
minus_divide = input().split('-') 
sum = 0 

# -가 나오기 전의 값 즉 0번인덱스의 값들을 다 더하기
for i in minus_divide[0].split('+'): # +기준으로 나눠서 더하기
    sum += int(i) 

# 나눠진거에 +기준으로 나누면 그 값들을 차례대로 빼면 된다.
for i in minus_divide[1:]: #1번째 인덱스 부터는 전부 빼야한다.
    
    for j in i.split('+'): # + 기준으로 나눠서 다 빼주자.
        sum -= int(j)
print(sum)



