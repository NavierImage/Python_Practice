import sys 
N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    arr.append(list(sys.stdin.readline().rstrip().split(" ")))

def inspection(y, x, arr):
    check_1 = None
    check_2 = None
    check_3 = None
    check_4 = None
    for i in range(y+1, N):
        if arr[i][x] == "S":
            check_1 = (i, x)
        elif arr[i][x] == "O":
            break 
    
    for i in range(y-1, -1, -1):
        if arr[i][x] == "S":
            check_2 = (i, x)
        elif arr[i][x] == "O":
            break
    
    for j in range(x+1, N):
        if arr[y][j] == "S":
            check_3 = (y, j)
        elif arr[y][j] == "O":
            break
    
    for j in range(x-1, -1, -1):
        if arr[y][j] == "S":
            check_4 = (y, j)
        elif arr[y][j] == "O":
            break
    
    return [check_1, check_2, check_3, check_4]

# 1차원 dfs 백트래킹
def dfs(num_list):
    if len(num_list) == 3:
        total_list.append(num_list[:])
        return 
    else:
        for i in range(N*N):
            if len(num_list) >= 1:
                if num_list[-1] >= i:
                    continue
            num_list.append(i)
            dfs(num_list)
            num_list.pop()

def ChangeByMeta(arr, meta, changestr):
    for j in range(len(meta)):
        y, x = meta[j]
        arr[y][x] = changestr
    return arr
    
idx_dict = {}
idx = 0
for i in range(N):
    for j in range(N):
        idx_dict[idx] = (i, j)
        idx += 1
teacher_co = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == "T":
            teacher_co.append((i, j))

student_num = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == "S":
            student_num += 1

total_list = []
dfs([])
for i in range(len(total_list)):
    
    no_flag = 0

    meta = []
    for j in range(len(total_list[i])):
        y, x = idx_dict[total_list[i][j]]
        if arr[y][x] == "T" or arr[y][x] == "S":
            no_flag =1
            break
        meta.append((y, x))
    if no_flag:
        continue

    arr = ChangeByMeta(arr, meta, "O")


    teacherfind = 0
    for j in range(len(teacher_co)):
        y, x= teacher_co[j]
        co_list = inspection(y, x, arr)
        
        for co in co_list:
            if co is not None:
                teacherfind = 1
                break
        if teacherfind:
            break
    if teacherfind:
        arr = ChangeByMeta(arr, meta, "X")

        continue
    

    arr = ChangeByMeta(arr, meta, "X")

    if teacherfind==0:
        print("YES")
        quit()
else:
    print("NO")
    

    
