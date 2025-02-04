while 1:
  try:
    s, t = input().split()
    
    t_len = len(t)
    s_len = len(s)
    
    s_index = 0
    true_or_false = False
    
    for i in range(t_len):
      
      if t[i] == s[s_index]:
        s_index += 1
        
        if s_index == s_len:
          true_or_false = True
          break
    
    if true_or_false:
      print("Yes")
    else:
      print("No")
  except:
    break