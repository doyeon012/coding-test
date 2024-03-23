#완전 탐색

dwarf_list = []

for i in range(9):
    dwarf_list.append(int(input()))

dwarf_list.sort()

sum_ = sum(dwarf_list)

for i in range(len(dwarf_list)-1):
    for j in range(i + 1, len(dwarf_list)):
        
        if sum_ - dwarf_list[i] - dwarf_list[j] == 100:
            for k in range(len(dwarf_list)):
                if k == i or k == j:
                    pass
                else:
                    print(dwarf_list[k])
            exit()