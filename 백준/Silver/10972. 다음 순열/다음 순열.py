# 다음 순열
# 수학, 조합론

# 입력
n = int(input())
arr = list(map(int, input().split()))

# 교환 지점 찾기(뒤에서 부터)
for i in range(n-1, 0, -1):
    
    # i-1=앞에값 < i=뒤에값 즉 뒤에값이 더 클때
    if arr[i-1] < arr[i] :
         
        # 고정된 앞에 값과, 맨 뒤부터  
        for j in range(n-1, 0, -1):
            
            # 고정된 앞에 값보다 큰 값을 찾았을 때
            if arr[i-1] < arr[j]: 
                
                # swap
                arr[i-1], arr[j] = arr[j], arr[i - 1]
                
                # 교환으로 인해 순서가 뒤바뀜. 최소의 다음 순열 보장
                arr = arr[:i] + sorted(arr[i:])
                
                # 다음 순열 출력 후 종료
                for i in arr:
                    print(i, end=" ")
                exit()
             
print(-1)
            
    