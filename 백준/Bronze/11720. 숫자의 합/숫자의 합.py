count = int(input())
sum = 0

num_list = list(map(int,input()))

for i in range(len(num_list)):
    sum += num_list[i]

print(sum)