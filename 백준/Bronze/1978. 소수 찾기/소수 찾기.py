count = int(input())
num_list = list(map(int, input().split()))
sum = 0

for num  in num_list:
    for i in range(2, num+1):
        if num % i == 0:
            if num == i:
                sum +=1
            break    
print(sum)
