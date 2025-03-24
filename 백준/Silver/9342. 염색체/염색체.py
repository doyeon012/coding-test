import re
N = int(input())

pattern = re.compile('^[A-F]?A+F+C+[A-F]?$')

for i in range(N):
  word = input()
  if pattern.match(word) == None:
    print('Good')
  else:
    print('Infected!')
    
      
