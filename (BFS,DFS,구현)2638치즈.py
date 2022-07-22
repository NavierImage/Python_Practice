import sys
from collections import deque
import copy
sys.setrecursionlimit(10**9)
n, m = map(int, sys.stdin.readline().rstrip().split())
board = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    board.append(temp)
#inside air = 0
#outside air = 2
#이런 식으로 명시적으로 해주는게 실제 코딩에는 더 좋음

def bfs(queue):
    global board
    global visited
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    #턴을 적용하기위해 copy하여 원본 기준으로 copy본에 업데이트
    copy_board = copy.deepcopy(board)
    four_dir = 4
    while queue:
        r, c = queue.popleft()
        visited[r][c] = 1
        air_count = 0
        for i in range(four_dir):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            f = 0
            if air_count >= 2:
                copy_board[r][c] = 2
            
            if visited[nr][nc] == 1:
                f = 1
            if f:
                continue
                
            if board[nr][nc] == 1:
                queue.append((nr, nc))

            #외부 공기일 때만 count 1 up    
            elif board[nr][nc] == 2:
                air_count += 1
                if air_count >= 2:
                    copy_board[r][c] = 2
                
    board = copy.deepcopy(copy_board)

#외부 공기를 따져주기 위한 dfs
def dfs(r, c):
    global visit_dfs
    global board
    if r < 0 or c < 0 or r >= n or c >= m:
        return False
    if board[r][c] == 1:
        return False
    if visit_dfs[r][c] == 1:
        return False
    
    board[r][c] = 2
    visit_dfs[r][c] = 1
    dfs(r+1, c)
    dfs(r-1, c)
    dfs(r, c+1)
    dfs(r, c-1)


cnt = 0
while True:
    
    visit_dfs = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    flag = 0
    #가장 자리에는 치즈가 없으므로 0, 0에서 dfs수행하면 외부공기 판단 가능
    dfs(0, 0)
    #전부 돌며 해당 되는 점들 넣어주고 동시적으로 bfs 진행
    queue = deque()
    for i in range(n):
        for j in range(m):
            check = 0
            if board[i][j] == 1:
                flag = 1
                queue.append((i, j))
            
    if flag == 0:
        break
    cnt += 1
    bfs(queue)
print(cnt)