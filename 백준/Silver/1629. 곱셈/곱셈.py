#분할 정복

# 3개의 수를 입력 받고 a를 b번 곱한수를 c로나눠서 나머지구하기

#포인트 - 거듭제곱(**), 나머지, 재귀
# 10^11 % 12 = ((10^5) % 12 * (10^5) % 12) % 12
# 홀수는 //2 했을때 1이 남아서 a다시 곱해주기
# b값을 절반씩 

import sys

def dac(a, b, c):
    if b == 1:
        return a % c

    elif b % 2 == 0:
        return (dac(a, b//2, c)**2) % c
    else:
        return ((dac(a, b//2, c)**2) *a) % c

a, b, c = map(int, (sys.stdin.readline().split()))
print(dac(a, b, c))
