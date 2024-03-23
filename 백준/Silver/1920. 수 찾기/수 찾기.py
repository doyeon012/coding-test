import sys

#이분 탐색
#입력 받는 곳
count1 = int(sys.stdin.readline())
num_list1 = list(map(int, sys.stdin.readline().split()))

num_list1.sort()

count2 = int(sys.stdin.readline())
num_list2 = list(map(int, sys.stdin.readline().split()))

# 이분 탐색 함수
def binary_search(arr, target):
    low = 0
    high = len(arr) -1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return 1
        
        if target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return 0

for i in range(len(num_list2)):
    print(binary_search(num_list1, num_list2[i]))