N = int(input())

result_count = 0
for i in range(N):
  word = input()
  word_len = len(word)
  alphabet = []
  
  for i in range(word_len):
    if word[i] not in alphabet:
      alphabet.append(word[i])
    else:
      if word[i-1] != word[i]:
        break
  else:
    result_count += 1

print(result_count)
    


  
  
  