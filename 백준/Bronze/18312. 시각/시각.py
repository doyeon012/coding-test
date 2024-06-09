# 시각
# 브루드포스

# 내가 했던 풀이
# N, K = map(int, input().split())
# count = 0

# for i in range(N):
#     i = str(i)
#     for j in range(60):
#         j = str(j)
#         for k in range(60):
#             k = str(k)
#             if (k > 10):
#                 if (i[0] == K or i[1] == K or j[0] == K or j[1] == K or k[0] == K or k[1] == K):
#                     count +=1
#             else:
#                 if (i[0] == K or j[0] == K or  k[0] == K):
#                     count +=1
            # 이렇게 i랑 j도 같이 생각하고 하려고 했다.
# print(count)

# 헷갈렸던 부분 - K가 3이라고 하면 3일때, 13일때, 23일때 전부 카운트 해야 하는데 처음에 단순하게 3일때만 접근해서
# 예시대로 count가 4000대로 나왔다. 

N, K = map(int, input().split())
K = str(K)
count = 0

for i in range(N+1): # 시
    if i < 10:
        i = '0' + str(i) # 앞에가 0일 때 0붙여주기
    
    for j in range(60): # 분
        if j < 10:
            j = '0' + str(j)
        
        for m in range(60): # 초
            if m < 10:
                m = '0' + str(m)
            
            if K in (str(i) + str(j) + str(m)): # K가 str로 바꾼 i, j, m에 있는지 있을 때 매다 매번 카운트.
                count += 1

print(count)