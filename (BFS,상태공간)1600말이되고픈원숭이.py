import sys
from collections import deque

k = int(sys.stdin.readline().rstrip())
m, n = map(int, sys.stdin.readline().rstrip().split())
#상태공간을 3차원으로 두어, "기회의 사용" 에 대한 정보를 저장 할 수 있다.
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
visited = [[[0] * m for _ in range(n)] for _ in range(k+1)]
cnt = k

def bfs(r, c, k):
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    a_dr = [-1, -2, -2, -1, 1, 2, 2, 1]
    a_dc = [2, 1, -1, -2, -2, -1, 1, 2]

    queue = deque()
    queue.append((r, c, k))
    visited[k][r][c] = 1
    while queue:
        r, c, k = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<m:
                if board[nr][nc] == 0:
                    if visited[k][nr][nc] == 0 :
                        queue.append((nr, nc, k))
                        visited[k][nr][nc] = visited[k][r][c] + 1
                        
        
        if k == 0:
            continue
        for i in range(8):
            mr = r + a_dr[i]
            mc = c + a_dc[i]
            if 0<=mr<n and 0<=mc<m:
                if board[mr][mc] == 0:
                    if visited[k-1][mr][mc] == 0:
                        queue.append((mr, mc, k-1))
                        visited[k-1][mr][mc] = visited[k][r][c] + 1
bfs(0, 0, k)
res = []
for i in range(cnt+1): #배열 갯수 주의
    if visited[i][n-1][m-1] != 0:
        res.append(visited[i][n-1][m-1])

if len(res) != 0:
    print(min(res)-1)
else:
    print(-1)
