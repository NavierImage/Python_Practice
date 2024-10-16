import sys 
sys.setrecursionlimit(5*(10**3))
arr = []
for i in range(5):
    arr.append(list(sys.stdin.readline().rstrip()))

idx_dict = {}

exist_char = []
total_idx = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == "x":
            idx_dict[total_idx] = (i, j)
            total_idx += 1
        elif arr[i][j] == ".":
            pass 
        else:
            exist_char.append(arr[i][j])

num_map_dict = {num : chr(65+num-1) for num in range(1, 13)}
char_map_dict = {chr(65+num-1)  : num for num in range(1, 13)}

need_char_list =[]
for key, val in char_map_dict.items():
    if key in exist_char:
        pass 
    else:
        need_char_list.append(key)

def check_star(arr):
    

    idx_list = [[(0, 4), (1, 3), (2, 2), (3, 1)],
            [(1, 1), (1, 3), (1, 5), (1, 7)], 
            [(0, 4), (1, 5), (2, 6), (3, 7)],
            [(3, 1), (3, 3), (3, 5), (3, 7)],
            [(1, 1), (2, 2), (3, 3), (4, 4)],
            [(4, 4), (3, 5), (2, 6), (1, 7)]]
    
    for i in range(len(idx_list)):
        temp_sum_num = 0
        for j in range(len(idx_list[i])):
            r, c = idx_list[i][j]
            temp_sum_num += char_map_dict[arr[r][c]]
        
        if i == 0:
            first_sum_num = temp_sum_num
        else:
            if first_sum_num == temp_sum_num:
                pass 
            else:
                return 0
        
    return 1

# idx_list = []
def dfs(visit_dict, cnt):
    if cnt == total_idx:
        # idx_list.append(num_list[:])

        
        rst = check_star(arr)
        if rst == 1:
            for i, a in enumerate(arr):
                for aa in a:
                    print(aa, end="")
                if i != len(a) - 1:
                    print()
            quit()
        

    else:
        for i in range(total_idx):
            if i in visit_dict:
                continue
            # num_list.append(i)
            r, c = idx_dict[cnt]
            arr[r][c] = need_char_list[i]
            visit_dict[i] = 1
            dfs(visit_dict, cnt+1)
            arr[r][c] = "x"
            visit_dict.pop(i)

dfs({}, 0)
# print(need_char_list)

    

# ans_list.sort()

