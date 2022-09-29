import sys 
from collections import deque

n, m, sec = map(int, sys.stdin.readline().rstrip().split())

board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))
timer_board = [[0] * m for _ in range(n)]

def bomb_plant_bfs(r, c, time):
    board[r][c] = 'O'
    timer_board[r][c] = time
    visited = [[0] * m for _ in range(n)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    queue = deque()
    
    queue.append((r, c))
    visited[r][c] = 1
    
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr <n and 0<=nc <m:
                if visited[nr][nc] == 0 and board[nr][nc] == '.':
                    board[nr][nc] = 'O'
                    visited[nr][nc] == 1
                    queue.append((nr, nc))
                    timer_board[nr][nc] = time
time = 0
for iter in range(10000):
    time += 1
    for i in range(n):
        for j in range(m):
            find = 0
            if time == 1:
                if board[i][j] == 'O':
                    timer_board[i][j] = 0
            else:
                #2초부터 폭탄설치 시작
                if board[i][j] == '.':
                    bomb_plant_bfs(i, j, time)
                    
                if find: break
        if find:break
    #지정한 시간이면 break
    if time == sec:
        break
    ##폭발##
    #첫 타임엔 아무일 X
    if time == 1:
        continue
    #2초에서 폭탄설치하고 1초 추가
    boom_list = deque()
    time += 1
    #3초때 처음 설치한 폭탄 터짐
    #근데 바로 터뜨리면 3초에 터져야할 모든 폭탄들이 터질수 없으므로
    #터져야할 좌표들 저장해두고 한번에 모아서 터뜨림
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'O' and (time - timer_board[i][j]) >= 3:
                boom_list.append((i, j))
                

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    #모아서 터뜨리기
    while boom_list:
        r, c = boom_list.popleft()
        board[r][c] = '.'
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<m:
                board[nr][nc] = '.'
                
    #지정한 시간에 break
    if time == sec:
        break
                    
for i in board:
    for j in i:
        print(j, end='')
    print()
