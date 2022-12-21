import sys
import copy
from itertools import product
dir_list = [[(0, -1), (1, -1), (2, -1), (3, -1)], #북 서 남 동
[(0, 2), (1, 3)],
[(0, 1), (1, 2), (2, 3), (3, 0)],
 [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)],
 [(0, 1, 2, 3)]]

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

sub_arr = [[' '] * m for _ in range(n)]

camera_list=  []
sel_dir = []
atv_map = [0] * 5
for i in range(n):
    for j in range(m):
        if 1 <= arr[i][j] <= 5:
            atv_map[arr[i][j]-1] = 1
            sel_dir.append(dir_list[arr[i][j]-1][:])
            camera_list.append((arr[i][j], i, j))

tot_list = list(product(*list(sel_dir))) #리스트끼리의 수형도(경우의수)
def make_shop(dir, y, x):
    i = 0
    sub_arr[y][x] = '#'
    while True:
        i += 1
        if dir == 0:
            ny = y - i
            nx = x
            if ny < 0 or ny >= n or arr[ny][nx] == 6:
                break
            sub_arr[ny][nx] = '#'
        elif dir == 1:
            ny = y
            nx = x - i
            if nx < 0 or nx >= m or arr[ny][nx] == 6:
                break
            sub_arr[ny][nx] = '#'
        elif dir == 2:
            ny = y + i
            nx = x
            if ny >= n or ny < 0 or arr[ny][nx] == 6:
                break
            sub_arr[ny][nx] = '#'
        elif dir == 3:
            ny = y
            nx = x + i
            if nx >= m or nx < 0 or arr[ny][nx] == 6:
                break
            sub_arr[ny][nx] = '#'
min_cnt= 10000
for its in range(len(tot_list)):
    sub_arr = [[' '] * m for _ in range(n)]
    for i, item in enumerate(tot_list[its]):
        for j, dirn in enumerate(item):
            if dirn == -1:
                continue
            _, yy, xx = camera_list[i]
            make_shop(dirn, yy, xx)
        cnt = 0
        for u, p in enumerate(sub_arr):
            for v, q in enumerate(p):
                if q == ' ' and arr[u][v] != 6:
                    cnt += 1
        if min_cnt > cnt:
            min_cnt = cnt
if min_cnt >= 100:
    sup_cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                sup_cnt += 1
    print(sup_cnt)
else:
    print(min_cnt)
