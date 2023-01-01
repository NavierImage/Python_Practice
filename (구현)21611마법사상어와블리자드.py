import sys
import copy
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
magic = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    magic.append((a, b))
idx_arr = [[0] * n for _ in range(n)]
cy, cx = (n//2, n//2)
coeff = 1
idx = 0
cx -= 1
cy += 1; cx += 1

idx_list = []
for turn in range(n//2):
    cy -= 1; cx -= 1
    for i in range(2*turn + 2):
        idx += 1
        idx_arr[cy+i][cx] = idx
        idx_list.append((cy+i, cx))
    cy += 2*turn + 1
    cx += 1
    for j in range(2*turn + 2):
        idx += 1
        idx_arr[cy][cx+j] = idx
        idx_list.append((cy, cx+j))
    cy -= 1
    cx += 2*turn + 1
    for i in range(2*turn + 2):
        idx += 1
        idx_arr[cy-i][cx] = idx
        idx_list.append((cy-i, cx))
    cy -= 2*turn + 1
    cx -= 1
    for j in range(2*turn + 2):
        idx += 1
        idx_arr[cy][cx-j] = idx
        idx_list.append((cy, cx-j))
    cx -= 2*turn + 1
    cy += 1
idx_list = tuple(idx_list)


#인덱스 저장해놓기 ( 돌리는 순서대로)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

#여기서 병목 생기는 듯
def pado2(arr, idx_list):
    temp = []
    for num in range(len(idx_list)):
        a, b = idx_list[num]
        if arr[a][b] != 0:
            temp.append(arr[a][b])
            arr[a][b] = 0
    for num in range(len(temp)):
        a, b = idx_list[num]
        arr[a][b] = temp[num]
    return arr

def explode(arr, idx_list):
    score = 0
    cnt = 0
    set_num = arr[n//2][n//2-1]
    tmp = []
    for num in range(len(idx_list)):
        a1, b1 = idx_list[num]
        if arr[a1][b1] == set_num:
            cnt += 1
            tmp.append((a1, b1))
        else:
            if cnt >= 4:
                for inum in range(len(tmp)):
                    a2, b2 = tmp[inum]
                    score += arr[a2][b2]
                    arr[a2][b2] = 0
            set_num = arr[a1][b1]
            cnt = 1
            tmp = [(a1, b1)]

    return arr, score

sc = 0
for cmd in magic:
    di, si = cmd
    di -= 1
    ny = (n//2) + dy[di] * si
    nx = (n//2) + dx[di] * si
    if di == 0:
        for i in range(n//2, ny-1, -1):
            arr[i][n//2] = 0
    elif di == 1:
        for i in range(n//2, ny+1):
            arr[i][n//2] = 0
    elif di == 2:
        for j in range(n//2, nx-1, -1):
            arr[n//2][j] = 0
    elif di == 3:
        for j in range(n//2, nx+1):
            arr[n//2][j] = 0
    
    arr = pado2(arr, idx_list)
    
    while True:
        arr, sc_t = explode(arr, idx_list)
        sc += sc_t
        tmparr = copy.deepcopy(arr)
        arr = pado2(arr, idx_list)
        if arr == tmparr:
            break

    cnt = 0
    set_num = arr[n//2][n//2-1]
    temp = []
    for num in range(len(idx_list)):
        a1, b1 = idx_list[num]
        if arr[a1][b1] == set_num:
            cnt += 1
            
        else:
            temp.append(cnt)
            temp.append(set_num)
            set_num = arr[a1][b1]
            cnt = 1
    new_arr = [[0] * n for _ in range(n)]
    for num in range(len(idx_list)):
        try:
            a, b = idx_list[num]
            new_arr[a][b] = temp[num]
        except:
            break
    arr = copy.deepcopy(new_arr)
print(sc)
