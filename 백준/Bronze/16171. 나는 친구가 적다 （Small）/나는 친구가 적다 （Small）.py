# 나는 친구가 적다.
# 문자열

# 입력
word = list(input())
target = input()

ll = []

# 문자열 찾기
for i in word:
    if i.isalpha(): # 알파벳 문자인지 확인.
        ll.append(i)

ll = ''.join(ll) # 리스트 ll을 문자열로 합치기
       
# 출력
if target in ll: # 문자열 포함 여부 확인. 즉 가공한 값이 ll
    print(1)
else:
    print(0)    
    