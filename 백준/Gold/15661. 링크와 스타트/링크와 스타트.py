# 링크와 스타트
# 브루드 포스, 백트래킹, 

n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
ans = 99999

# 능력치 차이 계산 함수
def is_it():
    global ans
    start, link = 0, 0
    
    # 이중 반복문을 통해 'visited' 배열을 검사하여 각 팀의 능력치 계산
    for i in range(n):
        for j in range(n):
            
            if visited[i] and visited[j]: # i와j가 모두 1이면 ex) 0과 1이 A팀이면 00, 01, 10, 11이 
                start += stats[i][j]      # 조건문에 걸려서 스타팀에 총합에 쌓인다.
                
            elif not visited[i] and not visited[j]: # i와 j가 모두 0이면
                link += stats[i][j]
    
    # 계산된 능력치 차이의 절대값을 'ans'와 비교하여 최소값 갱신
    ans = min(ans, abs(start - link))
    return

# 모든 가능한 팀 구성 탐색(재귀)
def resolve(iter):
    
    # 
    if iter == n: # 모든 사람을 팀에 배정한 경우
        is_it() # 현재 팀 구성의 능력치 차이 계산 함수 호출
        return
    
    visited[iter] = 1 # 현재 사람을 팀A에 배정(visited에 1을 넣었다는 뜻)하고 다음 사람으로 넘어감
    resolve(iter + 1)
    
    visited[iter] = 0 # 현재 사람을 팀 B에 배정하고 다음 사람으로 넘어감
    resolve(iter + 1)

# 결과 출력
resolve(0)
print(ans)