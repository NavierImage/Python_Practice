import sys 
n1, m1 = map(int, sys.stdin.readline().rstrip().split())




arr1 = []
for i in range(n1):
    arr1.append(list(sys.stdin.readline().rstrip()))
n2, m2 = map(int, sys.stdin.readline().rstrip().split())
arr2_1 = []
for i in range(n2):
    arr2_1.append(list(sys.stdin.readline().rstrip()))

for i in range(n1):
    for j in range(m1):
        arr1[i][j] = int(arr1[i][j])
for i in range(n2):
    for j in range(m2):
        arr2_1[i][j] = int(arr2_1[i][j])


# for t in total_arr:
#     print(*t)
arr2_2 = [] 
for j in range(m2):
    t = []
    for i in range(n2-1, -1, -1):
        t.append(arr2_1[i][j])
    arr2_2.append(t)
arr2_3 = []
for i in range(n2-1, -1, -1):
    t = []
    for j in range(m2-1, -1, -1):
        t.append(arr2_1[i][j])
    arr2_3.append(t)
arr2_4 = [] 
for j in range(m2-1, -1, -1):
    t = []
    for i in range(n2):
        t.append(arr2_1[i][j])
    arr2_4.append(t)

arr2_list = [arr2_1, arr2_2, arr2_3, arr2_4]
rst_list = []
for ind, arr2 in enumerate(arr2_list):
    n2 = len(arr2)
    m2 = len(arr2[0])
    max_row_size = n1 + n2 * 2
    max_col_size = m1 + m2 * 2

    total_arr = [[[0 for col in range(max_col_size)]for row in range(max_row_size)]for z in range(2)]

    for i in range(n2, n2 + n1, 1):
        for j in range(m2, m2 + m1, 1):
            total_arr[0][i][j] = arr1[i-n2][j-m2]

    for i in range(max_row_size-n2):
        for j in range(max_col_size-m2):
            if i == 0:
                if j < m2:
                    continue
                elif j >= m2 + m1:
                    continue
            elif i >= (n1 + n2):
                if j < m2:
                    continue
                elif j >= m2 + m1:
                    continue

            # total_arr[i][j] = 3
            index_cache = []
            flag = 0
            for u in range(n2):
                for v in range(m2):
                    # print(i+u, j+v, u, v)
                    total_arr[1][i + u][j + v] += arr2[u][v]
                    if total_arr[1][i+u][j+v] + total_arr[0][i+u][j+v] == 2:
                        total_arr[1][i+u][j+v] = 0
                        flag = 1
                        break 
                    else:
                        index_cache.append((i+u, j+v))
                if flag:
                    break
            if flag:
                for ind_tup in index_cache:
                    r, c = ind_tup
                    total_arr[1][r][c] = 0
                continue
            
            sy1 = n2
            sx1 = m2
            ey1 = n2 + n1 
            ex1 = m2 + m1 
            
            sy2 = i
            sx2 = j
            ey2 = n2 + i 
            ex2 = m2 + j 

            y1 = min(sy1, sy2)
            y2 = max(ey1, ey2)
            x1 = min(sx1, sx2)
            x2 = max(ex1, ex2)

            area = (y2 - y1) * (x2 - x1)
            # if ind == 3:
            #     print("*****")
            #     for t in total_arr[0]:
            #         print(*t)
            #     print()
            #     for t in total_arr[1]:
            #         print(*t)
            #     print("*****")
            rst_list.append(area)
            for ind_tup in index_cache:
                r, c = ind_tup
                
                total_arr[1][r][c] = 0
        
        
        
                    
print(min(rst_list))