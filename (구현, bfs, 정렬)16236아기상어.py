import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

def bfs(r, c, shark_size, stomach):
    queue = deque()
    visited = [[0] * n for _ in range(n)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    queue.append((r, c))
    time = 0
    visited[r][c] = 1
    nominate = []
    #찾으면서 조건에 맞는거 후보에 담고, 문제에서 주어진 기준에 맞추어 정렬하기.
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr <n and 0 <= nc <n:
                if visited[nr][nc] == 0:
                    if board[nr][nc] < shark_size and board[nr][nc] != 0:
                        stomach.append(board[nr][nc])
                        nominate.append((visited[r][c], nr, nc, stomach[:]))
                        stomach.pop(-1)
                    
                    elif board[nr][nc] == shark_size or board[nr][nc] == 0:
                        visited[nr][nc] = visited[r][c] + 1
                        queue.append((nr, nc))

                    elif board[nr][nc] > shark_size:
                        pass

    if len(nominate) == 0:
        return stomach, 0
    else:
        nominate.sort(key = lambda x: (x[0], x[1], x[2]))
        time, nr, nc, restomach = nominate[0]
        board[nr][nc] = 9
        return restomach, time

shark_size = 2
stomach = []
total_time = 0
for _ in range(10000):
    flag = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                board[i][j] = 0
                stomach, time = bfs(i, j, shark_size, stomach)
                total_time += time

                if len(stomach) >= shark_size:
                    shark_size += 1
                    stomach = []
                
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        break
print(total_time)                   
