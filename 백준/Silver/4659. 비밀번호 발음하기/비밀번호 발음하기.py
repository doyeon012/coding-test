while 1:
  
  c = input()
  
  if c == 'end':
    break
  
  trueOrFalse = False
  vowel = 0
  consonant = 0
  
  # 인덱스랑, 각 알파벳 뽑기
  for i, le in enumerate(c):
    
    # 연속으로 같은 단어 나왔을 경우인데 e, o가 아닌 경우 false
    if i > 0 and c[i-1] == le:
      if le not in 'eo':
        trueOrFalse = False
        break
    
    if le in 'aeiou': # 모음, 자음 각 3개 연속으로 오면 안되는거 체크 위해
      trueOrFalse = True # 모음이 최소 한개라도 있어야 함.
      vowel += 1
      consonant = 0
    else:
      consonant += 1
      vowel = 0
    
    if vowel >= 3 or consonant >= 3:
      trueOrFalse = False
      break
    
  
  if trueOrFalse:
    print(f'<{c}> is acceptable.') # f스트링 이용해서 
  else:
    print(f'<{c}> is not acceptable.')
  
  
  