def make_table(i, j, length, count):

    # 중앙에 도달했을 때 종료.
    if i == n//2 and j == n//2:
        array[i][j] = count
        return

    row, col = i, j
    
    # 아래쪽(행이 n의 값보다 작으면? 아래에 더 이상 가면 안됌.)
    while i < length:
        array[i][j] = count
        i += 1
        count -= 1
        
    i -= 1
    j += 1
    # 오른쪽(열이 n의 값보다 크면? 오른쪽으로 더 이상 가면 안됌.)
    while j < length:
        array[i][j] = count
        j += 1
        count -= 1
        
    # 재정비 왜냐? while 문에서 튕겼으므로 다시 왼쪽, 위 한칸 이동해서 위로이동
    i -= 1
    j -= 1
    # 위(행이 row 초기값은 0 그래서 0보다 작은 순간 끝)
    while i > row - 1:
        array[i][j] = count
        i -= 1
        count -= 1
        
    i += 1
    j -= 1
    while j > col:
        array[i][j] = count
        j -= 1
        count -= 1

    make_table(row + 1, col + 1, length - 1, count)


def print_result():
    for i, arr in enumerate(array): # 행 별로 조회
        
        if k in arr: # k가 현재 행에 존재하는지?
            position = (i + 1, arr.index(k) + 1)
        print(' '.join(list(map(str, arr)))) # 숫자를 문자형인 str로 바꿔서 .join으로 한 칸 띄우기
        
    print(position[0], position[1])

# main
n = int(input())
k = int(input())

array = [[0] * n for _ in range(n)] # 초기화 한 배열
make_table(0, 0, n, n**2)

print_result()