def min_time_to_create_song(n):
    # 초기값 설정
    ans = 10  # n이 1일 때 기본적으로 필요한 시간

    # 복사 가능한 크기의 기준점
    cri = 1
    while n >= cri * 2:
        ans += 1
        cri *= 2
    
    return ans

def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    
    result = min_time_to_create_song(n)
    print(result)

if __name__ == "__main__":
    main()