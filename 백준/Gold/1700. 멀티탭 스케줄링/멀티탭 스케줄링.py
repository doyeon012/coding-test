import sys
input = sys.stdin.readline

#입력 받기
n, k = map(int,input().strip().split())
items = list(map(int,input().split()))

# 멀티탭 수만큼 list 만들기
multiTap = [0] * n
cnt=0

for i in range(len(items)):
    
    # 1 - 멀티탭에 꽂혀있어? 
    if items[i] in multiTap:
          continue # 아무런 조치를 취할 필요가 없어 넘어가!
    
    # 2 - 멀티탭에 꽂혀 있지 않아?
    else:
      # 2 - 1 멀티탭에 자리가 남아있어?
      if 0 in multiTap:
          multiTap[multiTap.index(0)] = items[i]

      # 2 - 2 멀티탭에 자리가 없어? 그러면 어떤 기기의 플러그를 빼야겠지?
      else:
        
        appear=[]
        # 현재 기기(item[i]) 이후로 > 사용될 기기들을 순서를 저장하기 위한 반복문
        for j in range(i+1,len(items)): 
            if items[j] in multiTap: # 순회 중인 기기(item[j])가 멀티탭에 꽂혀 있다면? 즉 multiTap에 존재해? 그러면 재사용o
                appear.append(items[j]) # 앞으로 다시 사용될 기기 appear 리스트 통해 확인o
                
        # 2 - 2 - 1
        # 멀티탭에 꽂힌 아이템 중 다시 등장하는 아이템이 있어?
        if(appear):
          result_list = list(dict.fromkeys(appear))
          for k in range(len(multiTap)):
              
            # 멀티탭에 꽂힌 기기가 다시 사용될 기기 목록에 없는지 확인 > 즉 다시 사용될 일 없는 기기에 현재 기기 꽂아.
            if multiTap[k] not in result_list:
                  multiTap[k]=items[i] # 멀티탭에 현재 기기를 꽂고 카운트
                  cnt+=1
                  break
          
          # 멀티탭에 꽂힌 모든 기기가 result_list에 포함되어 있어?
          # 가장 나중에 사용될 기기의 플러그를 뽑는 것이 최적
          # result_list[-1] = 가장 나중에 다시 사용될 기기      
          else:
            multiTap[multiTap.index(result_list[-1])]=items[i]
            cnt+=1
        
        # 2 - 2 - 2    
        # 멀티탭에 꽂힌 아이템 중 다시 등장 하는 아이템이 아예 없어? > 아무거나 뽑아 즉 0번째 위치의 기기를 뽑아!
        else:
          multiTap[0]=items[i]
          cnt+=1

print(cnt)