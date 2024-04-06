#LCS
#DP

#입력 값 초기화, 세팅
import sys
string_a = ' ' + sys.stdin.readline().rstrip()
string_b = ' ' + sys.stdin.readline().rstrip()

lcs = [[0] * len(string_b) for _ in range(len(string_a))]

for i in range(1, len(string_a)): #A 문자열의 길이 만큼 반복문
    for j in range(1, len(string_b)): #B 문자열의 길이 만큼 반복문
        
        if string_a[i] == string_b[j]: #문자가 같아?
            lcs[i][j] = lcs[i - 1][j - 1] + 1 #지금까지의 최대 공통 부분수열에 + 1
            
        else: #문자가 달라?
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1]) #부분수열은 연속된 값x 이전의 과정의 값 max

print(lcs[-1][-1])