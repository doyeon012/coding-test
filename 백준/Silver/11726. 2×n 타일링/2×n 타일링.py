#2*n 타일링
#DP
import sys
input = sys.stdin.readline

#초기값 세팅
num = int(input())
arr = [0, 1, 2] 

for i in range(3, num+1):
    arr.append(arr[i-1] + arr[i-2])
    #(2*1크기를 끝에 더해줌. n-1의 최대 방법의 수) + 
    # (1*2크기 2개를 끝에 더해줌. n-2의 최대 방법의 수)
    
    #주어진 타일이 2개 > (n-1의 가짓수에 끝에 2*1 붙여준것) +
    # (n-2의 가짓수에 끝에 1*2 2개 붙여준 것)
    
    #붙였다고해서 경우의 수가 달라지진 않고, n-1의 가짓수 + n-2의 가짓수
    
print(arr[num] % 10007) # 문제에서 10,007로 나눈 나머지 출력