import sys 
import copy
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
######################################## 입력 세팅 #################################

num_arr = []
for i in range(4):
    num_arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

dir_arr = []
fish_arr = []
for i in range(4):
    temp_dir_arr = []
    temp_fish_arr = []
    for j in range(8):
        if j % 2:
            num_arr[i][j] -= 1
            temp_dir_arr.append(num_arr[i][j])
        else:
            temp_fish_arr.append(num_arr[i][j])
    dir_arr.append(temp_dir_arr)
    fish_arr.append(temp_fish_arr)
############################################################################################
############################################################################################

####################################물고기번호 순서대로, 배열 인덱싱####################################

def get_fish_idx(fish_arr):
    idx_dict = {}
    for i in range(16):
        idx_dict[i+1] = None
    for i in range(len(fish_arr)):
        for j in range(len(fish_arr[i])):
            idx_dict[fish_arr[i][j]] = (i, j)
    
    return idx_dict
##################################물고기 이동 함수##################################

def fish_moving(fish_arr, dir_arr, idx_dict):
    for idx in range(1, 17):
        
        key = idx 

        value = idx_dict[key]
        if value == None:
            continue
        done = 0
        i, j = value
        while done == 0:
            
            ni = i + dy[dir_arr[i][j]]
            nj = j + dx[dir_arr[i][j]]
            if 0<=ni<4 and 0<=nj<4:
                if fish_arr[ni][nj] == 17:
                    pass 
                else:
                    
                    fish_arr[ni][nj], fish_arr[i][j] = fish_arr[i][j], fish_arr[ni][nj]
                    dir_arr[ni][nj], dir_arr[i][j] = dir_arr[i][j], dir_arr[ni][nj]
                    
                    idx_dict[fish_arr[ni][nj]] = (ni, nj)
                    idx_dict[fish_arr[i][j]] = (i, j)
                    
                    done = 1
                    break
            
            dir_arr[i][j] += 1
            if dir_arr[i][j] >= 8:
                dir_arr[i][j] = 0
    return fish_arr, dir_arr, idx_dict


idx_dict = get_fish_idx(fish_arr)
eat_total = 0
def dfs(shark_co, fish_arr, dir_arr, idx_dict, eat):
    global eat_total
    ####상어 기존 위치 파악 ####
    for i in range(4):
        for j in range(4):
            if fish_arr[i][j] == 17:
                fish_arr[i][j] = 0
                dir_arr[i][j] = -1
    #### 새로운 상어 위치, 물고기 잡아먹기 ####
    eat += fish_arr[shark_co[0]][shark_co[1]] 
    idx_dict[fish_arr[shark_co[0]][shark_co[1]]] = None
    fish_arr[shark_co[0]][shark_co[1]] = 17
    #### 상어 물고기 포식 완료 ####
    eat_total = max(eat, eat_total) # 먹은최댓값 판단
    #### 물고기 이동 ####
    fish_arr, dir_arr, idx_dict = fish_moving(fish_arr, dir_arr, idx_dict)
    #### 다음 경우의 수 탐색시 위한 메타 데이터 ###
    fish_arr_save = copy.deepcopy(fish_arr)
    dir_arr_save= copy.deepcopy(dir_arr)
    idx_dict_save = copy.deepcopy(idx_dict)
    eat_save = eat
    #######################################

    for i in range(4):
        #### 상어 갈수 있는 경우의 수 - for 문 ####
        ni = shark_co[0] + dy[dir_arr[shark_co[0]][shark_co[1]]] * (i+1)
        nj = shark_co[1] + dx[dir_arr[shark_co[0]][shark_co[1]]] * (i+1)
        
        if 0 <= ni < 4 and 0<= nj < 4:
            ##### 물고기가 없는 칸으로 상어 못감 #####
            if fish_arr[ni][nj] == 0:
                continue
            ##### 재귀 진행 #####
            dfs((ni, nj), fish_arr, dir_arr, idx_dict, eat)
            ##### 다음 경우의수 탐색 위해서 기존 메타 데이터 복원 ####
            fish_arr = copy.deepcopy(fish_arr_save)
            dir_arr = copy.deepcopy(dir_arr_save)
            idx_dict = copy.deepcopy(idx_dict_save)
            eat = eat_save
            ############################################
dfs((0, 0), fish_arr, dir_arr, idx_dict, 0)
print(eat_total)