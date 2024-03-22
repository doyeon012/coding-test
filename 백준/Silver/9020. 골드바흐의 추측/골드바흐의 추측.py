import math

def decimal_determine(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

count = int(input())

for _ in range(count):
    num = int(input())
    
    a = num //2
    b = num //2
    
    for _ in range(num // 2):
        if decimal_determine(a) and decimal_determine(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
