import sys

count1 = int(sys.stdin.readline())
num1_list = list(map(int, sys.stdin.readline().split()))

count2 = int(sys.stdin.readline())
num2_list = list(map(int, sys.stdin.readline().split()))

dic = {}

for num2 in num2_list:
    dic[num2] = 0

for num1 in num1_list:
    if num1 in dic:
        dic[num1] = 1
        
for d in dic:
    print(dic[d], end=' ')