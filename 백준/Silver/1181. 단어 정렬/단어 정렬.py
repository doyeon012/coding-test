import sys

count = int(sys.stdin.readline())
word_list = []

for i in range(count):
    word_list.append(sys.stdin.readline().strip())
    
set_word_list = set(word_list)
word_list = list(set_word_list)
word_list.sort()
word_list.sort(key=len)

for word in word_list:
    print(word)