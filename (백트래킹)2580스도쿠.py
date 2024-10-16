import sys 

arr = []
for i in range(9):
    temp = list(sys.stdin.readline().rstrip().split(' '))
    for j in range(len(temp)):
        temp[j] = int(temp[j])
    arr.append(temp)


which_group_dict = {}
group_dict = {}
gidx = 0
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        for u in range(3):
            for v in range(3):
                which_group_dict[(i+u, j+v)] = gidx
                if gidx in group_dict:
                    group_dict[gidx].append((i+u, j+v))
                else:
                    group_dict[gidx] = [(i+u, j+v)]

        gidx += 1

def SQcheck(arr, r, c, tgt):
    where = which_group_dict[(r, c)]
    group_idx_list = group_dict[where]

    square_zero_cnt = 0
    square_check = {}
    for idx in group_idx_list:
        i, j = idx
        if arr[i][j] == tgt:
            return 0
    return 1

def ROWcheck(arr, r, c, tgt):
    for row in range(9):
        if arr[row][c] == tgt:
            return 0
    return 1

def COLcheck(arr, r, c, tgt):
    
    for col in range(9):
        if arr[r][col] == tgt:
            return 0
    
    return  1 


idx_list = []
total_idx = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            idx_list.append((i, j))
            total_idx += 1

def dfs(arr, cnt):
    if cnt == total_idx:
        
        for a in arr:
            print(*a)
        quit()

    else:
        
        for i in range(1, 10):
            r, c = idx_list[cnt]
    
            if SQcheck(arr, r, c, i) and ROWcheck(arr, r, c, i) and COLcheck(arr, r, c, i):
                arr[r][c] = i
                dfs(arr, cnt + 1)
                arr[r][c] = 0
            else:
                arr[r][c] = 0

dfs(arr, 0)