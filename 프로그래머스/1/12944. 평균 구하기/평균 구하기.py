def solution(arr):
    answer = 0
    num_sum = 0
    num_count = 0
    
    for num in arr:
        num_sum += num
        num_count += 1
    
    answer = num_sum / num_count
        
    return answer