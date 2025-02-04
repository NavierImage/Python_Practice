import sys 
import copy
N, M, R = map(int, sys.stdin.readline().rstrip().split())
arr = []

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

cmd_list = list(map(int, sys.stdin.readline().rstrip().split()))


def one(arr, n, m):
    for i in range(n//2):
        for j in range(m):
            arr[i][j], arr[n-i-1][j] = arr[n-i-1][j], arr[i][j]
    return arr

def two(arr, n, m):
    for j in range(m//2):
        for i in range(n):
            arr[i][j], arr[i][m-j-1] = arr[i][m-j-1], arr[i][j]
    return arr

def three(arr, n, m):
    new_arr = []
    for j in range(m):
        temp = []
        for i in range(n-1, -1, -1):
            temp.append(arr[i][j])
        new_arr.append(temp)
    return new_arr

def four(arr, n, m):
    new_arr = []
    for j in range(m-1, -1, -1):
        temp = []
        for i in range(n):
            temp.append(arr[i][j])
        new_arr.append(temp)
    return new_arr

def three180(arr, n, m):
    new_arr = []
    for i in range(n-1, -1, -1):
        temp = []
        for j in range(m-1, -1, -1):
            temp.append(arr[i][j])
        new_arr.append(temp)
    return new_arr

def five(arr, n, m):
    temp_1 = []
    for i in range(n//2):
        for j in range(m//2):
            temp_1.append(arr[i][j])
    temp_2 = []
    for i in range(n//2):
        for j in range(m//2, m):
            temp_2.append(arr[i][j])
    temp_3 = []
    for i in range(n//2, n):
        for j in range(m//2, m):
            temp_3.append(arr[i][j])
    temp_4 = []
    for i in range(n//2, n):
        for j in range(m//2):
            temp_4.append(arr[i][j])
    
    tidx = 0
    for i in range(n//2):
        for j in range(m//2, m):
            arr[i][j] = temp_1[tidx]
            tidx += 1 
    tidx = 0
    for i in range(n//2, n):
        for j in range(m//2, m):
            arr[i][j] = temp_2[tidx]
            tidx += 1 
    tidx = 0
    for i in range(n//2, n):
        for j in range(m//2):
            arr[i][j] = temp_3[tidx]
            tidx += 1 
    tidx = 0
    for i in range(n//2):
        for j in range(m//2):
            arr[i][j] = temp_4[tidx]
            tidx += 1 
    return arr

def six(arr, n, m):
    temp_1 = []
    for i in range(n//2):
        for j in range(m//2):
            temp_1.append(arr[i][j])
    temp_2 = []
    for i in range(n//2):
        for j in range(m//2, m):
            temp_2.append(arr[i][j])
    temp_3 = []
    for i in range(n//2, n):
        for j in range(m//2, m):
            temp_3.append(arr[i][j])
    temp_4 = []
    for i in range(n//2, n):
        for j in range(m//2):
            temp_4.append(arr[i][j])
    
    tidx = 0
    for i in range(n//2):
        for j in range(m//2, m):
            arr[i][j] = temp_3[tidx]
            tidx += 1 
    tidx = 0
    for i in range(n//2, n):
        for j in range(m//2, m):
            arr[i][j] = temp_4[tidx]
            tidx += 1 
    tidx = 0
    for i in range(n//2, n):
        for j in range(m//2):
            arr[i][j] = temp_1[tidx]
            tidx += 1 
    tidx = 0
    for i in range(n//2):
        for j in range(m//2):
            arr[i][j] = temp_2[tidx]
            tidx += 1 

    return arr

y_point = [0, N//2-1, N//2, N]
x_point = [0, M//2-1, M//2, M]
# temp_1 = [[1, 2], [3, 4]]
# temp_2 = [[5, 6], [7, 8]]
# temp_3 = [[9, 10], [11, 12]]
# temp_4 = [[13, 14], [15, 16]]
if N != 2 and M != 2:
    zarr = [[1, 2, 5, 6],
            [3, 4, 7, 8],
            [9, 10, 13, 14],
            [11, 12, 15, 16]]

    # print(zarr)
    coord_dict = {
        1:  (0, 0),
        2:  (0, M//2 - 1),
        3:  (N//2 - 1, 0),
        4:  (N//2 - 1, M//2 - 1),
        
        5:  (0, M//2),
        6:  (0, M - 1),
        7:  (N//2 - 1, M//2),
        8:  (N//2 - 1, M - 1),
        
        9:  (N//2, 0),
        10: (N//2, M//2 - 1),
        11: (N - 1, 0),
        12: (N - 1, M//2 - 1),
        
        13: (N//2, M//2),
        14: (N//2, M - 1),
        15: (N - 1, M//2),
        16: (N - 1, M - 1)
    }
    # zipped_list = [temp_1, temp_2, temp_3, temp_4]

    for cmd in cmd_list:
        if cmd == 1:
            
                zarr = one(zarr, 4, 4)
        if cmd == 2:
            
                zarr = two(zarr, 4, 4)
                
        elif cmd == 3:
            
                zarr = three(zarr, 4, 4)
        elif cmd == 4:
            
                zarr = four(zarr, 4, 4)
        elif cmd ==5:
            zarr = five(zarr, 4, 4)
        elif cmd == 6:
            zarr = six(zarr, 4, 4)


    temp_dict = {}
    tidx = 1
    for i in range(0, 4, 2):
        for j in range(0, 4, 2):
            # print(zarr[i][j], coord_dict[zarr[i][j]], end="")
            y1, x1 = coord_dict[zarr[i][j]]
            y4, x4 = coord_dict[zarr[i+1][j+1]]
            row_diff = y4 - y1
            col_diff = x4 - x1 
            r_co = 1 
            c_co = 1 
            if row_diff < 0: 
                ey = y1 + row_diff -1
                r_co = -1
            else:
                ey = y1 + row_diff + 1
            if col_diff < 0:
                ex = x1 + col_diff - 1
                c_co = -1
            else:
                ex = x1 + col_diff + 1
            sy, sx = y1, x1

            temp = []
            y2, x2 = coord_dict[zarr[i][j+1]]
            if y2 == y1:
                for u in range(sy, ey, r_co):
                    t = []
                    for v in range(sx, ex, c_co):
                        t.append(arr[u][v])
                    temp.append(t)
                temp_dict[tidx] = copy.deepcopy(temp)
            else:
                for v in range(sx, ex, c_co):
                    t = []
                    for u in range(sy, ey, r_co):
                        t.append(arr[u][v])
                    temp.append(t)
                temp_dict[tidx] = copy.deepcopy(temp)
            tidx += 1
    rst_1 = []
    for arr1, arr2 in zip(temp_dict[1], temp_dict[2]):
        rst_1.append(arr1 + arr2)
    rst_2 = []
    for arr1, arr2 in zip(temp_dict[3], temp_dict[4]):
        rst_2.append(arr1 + arr2)

    for r in rst_1:
        print(*r)
    for r in rst_2:
        print(*r)
else:
    
    for cmd in cmd_list:
        n = len(arr)
        m = len(arr[0])
        if cmd == 1:
            
            arr = one(arr, n, m)
        if cmd == 2:
            
            arr = two(arr, n, m)
                
        elif cmd == 3:
            
            arr = three(arr, n, m)
        elif cmd == 4:
            
            arr = four(arr, n, m)
        elif cmd ==5:
            arr = five(arr, n, m)
        elif cmd == 6:
            arr = six(arr, n, m)
    for a in arr:
        print(*a)

