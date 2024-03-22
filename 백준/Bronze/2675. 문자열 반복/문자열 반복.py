total_count = int(input())

for _ in range(total_count):
    count, word =input().split()
    
    count = int(count)
    
    for j in range(len(word)):
        print(word[j]*count, end='')
    print("")   