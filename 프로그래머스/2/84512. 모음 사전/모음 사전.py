from itertools import product

def solution(word):
    answer = 0
    words = []
    
    for i in range(1,6):
        
        for j in product('AEIOU', repeat=i):
            words.append(''.join(list(j)))
            
    words.sort()
    answer = words.index(word) +1
    return answer