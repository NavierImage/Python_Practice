import sys
from collections import deque
import copy
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))
command = list(sys.stdin.readline().rstrip())

ard_list = []
jong_co = None
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == "I":
            jong_co = (i, j)
        elif arr[i][j] == "R":
            ard_list.append((i, j))

dy = [1, 1, 1, 0, 0, 0, -1, -1 ,-1]
dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

game_over = 0
move_num = 0
for inum, com in enumerate(command):
    com_num = int(com)-1
    Ji, Jj = jong_co
    NJi = Ji + dy[com_num]
    NJj = Jj + dx[com_num]
    if com_num != 4:
        move_num += 1
    

    if arr[NJi][NJj] == "R":
        game_over = 1
        move_num -= 1
        break #game over
    jong_co = (NJi, NJj)

    arr[NJi][NJj], arr[Ji][Jj] = arr[Ji][Jj], arr[NJi][NJj]
    
    new_ard_dict = {}
    for i in range(len(ard_list)):
        Ai, Aj = ard_list[i]
        distance_list = []
        for idx in range(9):
            if idx == 4:
                continue
            ni = Ai + dy[idx]
            nj = Aj + dx[idx]
            distance = abs(NJi-ni) + abs(NJj-nj)
            distance_list.append((distance, ni, nj))
        distance_list.sort(key=lambda x: x[0])
        new_i, new_j = distance_list[0][1], distance_list[0][2]
        try:
            new_ard_dict[(new_i, new_j)] += 1
        except:
            new_ard_dict[(new_i, new_j)] = 1
    
    temp_ard = []
    for key, val in new_ard_dict.items():
        if val > 1:
            pass
        elif jong_co == key:
            game_over = 1
            break
        else:
            temp_ard.append(key)
    if game_over:
        break
    temp_arr = [['.'] * m for _ in range(n)]
    for temp_cor in temp_ard:
        y, x = temp_cor
        temp_arr[y][x] = "R"
    temp_arr[NJi][NJj] = "I"
    ard_list = temp_ard[:]

    arr = copy.deepcopy(temp_arr)

if game_over:
    print("kraj %d" %(move_num+1))
else:
    for i, a in enumerate(arr):
        for b in a:
            print(b, end="")
        if i != len(arr)-1:
            print()