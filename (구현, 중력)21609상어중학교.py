import sys
import copy
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    ref_block = [(r, c)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    ref_val = board[r][c]
    while queue:
        r, c = queue.popleft()
        visited[r][c] = 1
        for i in range(len(dr)):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<= nr < n and 0<= nc < n:
                if visited[nr][nc] == 0 and (board[nr][nc] == ref_val or board[nr][nc] == 0):
                    ref_block.append((nr, nc))
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
    ref_block_sorted = sorted(ref_block, key=lambda x : (x[0], x[1]))
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                visited[i][j] = 0
    
    return ref_block_sorted
                    
score = 0
while True:
    visited = [[0] * n for _ in range(n)]
    block_list = []
    len_list = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:  
                if  board[i][j] == -1:
                    visited[i][j] = 1
                    continue
                elif board[i][j] == 6:
                    visited[i][j] = 1
                    continue
                else:
                    blocks = bfs(i, j)
                    

                    if blocks in block_list:
                        continue
                    else:
                    ########무지개 세트는 미리빼주자....######
                        rb_check = 0
                        for k in range(len(blocks)):
                            a, b = blocks[k]
                            if board[a][b] == 0:
                                continue
                            else:
                                rb_check = 1
                                break
                        if rb_check != 0:
                            block_list.append(blocks)

    length = len(block_list)
    #가장 큰거
    for i in range(length):
        len_list.append(len(block_list[i]))
       
    
    checker = 0
    for i in range(length):
        if len_list[i] != 1:
            checker = 1
    if checker == 0:
        break
    
    rainbow_checker = 0
    
    for i in range(len(block_list)):
        for j in range(len(block_list[i])):
            a, b = block_list[i][j]
            if board[a][b] != 0 and len(block_list[i]) > 1 :
                rainbow_checker = 1
                
    if rainbow_checker == 0:
        break
    #board[i][j]에서 따져서 0이 제일 많은 것으로.....
    rainbow_cnt = []
    for i in range(len(block_list)):
        zero_cnter = 0
        for j in range(len(block_list[i])):
            a, b = block_list[i][j]
            if board[a][b] == 0:
                zero_cnter += 1
        rainbow_cnt.append(zero_cnter)
    idx_list = []

    if len(len_list) != 0:
        len_max = max(len_list)

        for i in range(len(len_list)):
            if len_list[i] == len_max:
                idx_list.append(i)

        target = []
        for i in range(len(idx_list)):
            for j in range(len(block_list[idx_list[i]])):
                a, b = block_list[idx_list[i]][j]
                if board[a][b] == 0:
                    continue
                else:
                    break #기준 블록은 무지개 블록이 아니어야
            
            target.append((len_list[idx_list[i]], rainbow_cnt[idx_list[i]],  a, b, idx_list[i]))
        sorted_target = sorted(target, key= lambda x : (-x[0], -x[1], -x[2], -x[3]))
        _, _, _, _, idx = sorted_target[0]
        

        score += len(block_list[idx]) ** 2
        
        for i in range(len(block_list[idx])):
            a, b = block_list[idx][i]
            board[a][b] = 6
    
    #중력구현 
    for i in range(n-2, -1, -1):
        for j in range(n):
            if board[i][j] != -1:
                r = i
                while True:
                    if 0<=r+1 < n and board[r+1][j] == 6:
                        board[r+1][j] = board[r][j]
                        board[r][j] = 6
                        r += 1
                    else:
                        break
    
    #90도 회전 구현
    rotate_board = [[0] * n for _ in range(n)]
    for j in range(n-1, -1, -1):
        for i in range(n):
            rotate_board[n-1-j][i] = board[i][j]
    
    #다시 중력 구현
    for i in range(n-2, -1, -1):
        for j in range(n):
            if rotate_board[i][j] != -1:
                r = i
                while True:
                    
                    if 0<=r+1 < n and rotate_board[r+1][j] == 6:
                        rotate_board[r+1][j] = rotate_board[r][j]
                        rotate_board[r][j] = 6
                        r += 1
                    else:
                        break
   
    board = copy.deepcopy(rotate_board)
    
print(score)
#고생한 반례
#5 4
#1 0 -1 0 0
#2 0 -1 0 0
#3 0 -1 0 0
#4 0 -1 -1 -1
#4 4 1 1 1