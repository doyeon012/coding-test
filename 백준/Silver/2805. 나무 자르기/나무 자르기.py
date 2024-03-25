import sys # 시간절약

num_trees, height_trees = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

#초기값 세팅
start, end = 1, max(trees)

#이분 탐색 시작점 끝점, 서로 크로스 할때 end값으로 최대값 출력 
while start <= end:
    mid = (start + end) // 2
    
    tree_sum = 0
    # 잘린 나무의 총합 구하기
    for tree in trees: 
        if tree >= mid:
            tree_sum += tree - mid
            
    #총합 vs 타겟값을 비교하여 +- 
    if  tree_sum >= height_trees:
        start = mid + 1 #총합이 더 커 ~? 그럼 스타트를 미드값 +1 해서  덜 자른다.
    else:
        end = mid - 1 # 총합이 더 작아 ~? 그럼 엔드를 미드값 -1해서 더 자른다.
    
print(end) 
    
    
