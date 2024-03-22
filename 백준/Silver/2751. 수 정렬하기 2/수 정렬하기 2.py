import sys

count = int(sys.stdin.readline())

num_list = []

for i in range(count):
    num_list.append(int(sys.stdin.readline()))
    
num_list.sort() 

for num in  num_list:
    print(num)