import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

def bfs(man_list, fire_list):
    
    queue1 = deque()
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    visited_man = [[0] * m for _ in range(n)]
    r, c = man_list[0]
    visited_man[r][c] = 1
    
    while True:
        #걸어놓고 두개에 대해 따로진행해야함...
        #안그러면 꼬이게됨
        if len(man_list) == 0:
            break
        #사람 BFS 진행
        queue1 = deque(man_list)
        man_list = []
        while queue1:
            r, c = queue1.popleft()
            if board[r][c] == 'F': #불에 당한 경우의 수 볼필요없음
                continue
            board[r][c] = '.'
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<n and 0<=nc<m:
                    if visited_man[nr][nc] == 0 and board[nr][nc] == '.':
                        board[nr][nc] = 'J'
                        visited_man[nr][nc] = visited_man[r][c] + 1
                        man_list.append((nr, nc))
                ###찾으면 결과 출력후 끝###
                elif nr < 0 or nc < 0 or nr >= n or nc >= m:
                    print(visited_man[r][c])
                    quit()
        #불 BFS 진행
        queue2 = deque(fire_list)
        fire_list = []
        while queue2:
            fr, fc = queue2.popleft()
            for i in range(4):
                nfr = fr + dr[i]
                nfc = fc + dc[i]
                if 0<=nfr<n and 0<=nfc<m:
                    if board[nfr][nfc] == '.' or board[nfr][nfc] == "J": #사람도 밀어버림
                        board[nfr][nfc] = 'F'
                        fire_list.append((nfr, nfc))
man_list =[]
fire_list = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'J':
            man_list.append((i, j))
        elif board[i][j] == "F":
            fire_list.append((i, j))

bfs(man_list, fire_list)

##안에서 종료 안됐으면 IMPOSSIBLE 출력##
print("IMPOSSIBLE")
