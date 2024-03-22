count = int(input())

num_list = []

for i in range(count):
    num_list.append(int(input()))
    
num_list.sort() 

for num in  num_list:
    print(num)