import sys
import copy
r, c, k = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(3):
    arr.append((list(map(int, sys.stdin.readline().rstrip().split()))))

n = 3
m = 3
done = 0
for ans in range(101):
    try:
        if arr[r-1][c-1] == k:
            done = 1
            break
    except:
        pass
    if n >= m:
        for i in range(n):
            row_dict = {}
            new_arr_temp = []
            for j in range(m):
                if arr[i][j] != 0:
                    try:row_dict[arr[i][j]] += 1
                    except:row_dict[arr[i][j]] = 1
            
            row_tuple_list = []
            for key, value in row_dict.items():
                row_tuple_list.append((key, value))
                
            row_tuple_list.sort(key = lambda x: (x[1], x[0]))
            for u in range(len(row_tuple_list)):
                for v in range(len(row_tuple_list[u])):
                    new_arr_temp.append(row_tuple_list[u][v])

            arr[i] = new_arr_temp[:]
        max_ = 0
        for i in range(len(arr)):
            if max_ < len(arr[i]):
                max_ = len(arr[i])
        for i in range(len(arr)):
            if len(arr[i]) < max_:
                for j in range(max_-len(arr[i])):
                    arr[i].append(0)
            
                
                
        n = len(arr)
        m = len(arr[0])
        
    else:
        rot_arr = []
        for j in range(m):
            temp = []
            for i in range(n):
                temp.append(arr[i][j])
            rot_arr.append(temp)

        for i in range(m):
            row_dict = {}
            new_arr_temp = []
            for j in range(n):
                if rot_arr[i][j] != 0:
                    try:row_dict[rot_arr[i][j]] += 1
                    except:row_dict[rot_arr[i][j]] = 1
            
            row_tuple_list = []
            for key, value in row_dict.items():
                row_tuple_list.append((key, value))
                
            row_tuple_list.sort(key = lambda x: (x[1], x[0]))
            for u in range(len(row_tuple_list)):
                for v in range(len(row_tuple_list[u])):
                    new_arr_temp.append(row_tuple_list[u][v])
            
            rot_arr[i] = new_arr_temp[:]

        max_ = 0
        for i in range(len(rot_arr)):
            if max_ < len(rot_arr[i]):
                max_ = len(rot_arr[i])
        for i in range(len(rot_arr)):
            if len(rot_arr[i]) < max_:
                for j in range(max_-len(rot_arr[i])):
                    rot_arr[i].append(0)

        temp_n = len(rot_arr)
        temp_m = len(rot_arr[0])
        ret_arr = []
        for j in range(temp_m):
            ret_temp = []
            for i in range(temp_n):
                ret_temp.append(rot_arr[i][j])
            ret_arr.append(ret_temp)
        
        arr = copy.deepcopy(ret_arr)
        n = len(arr)
        m = len(arr[0])
    

if done == 0:
    print(-1)
elif done == 1:
    print(ans)