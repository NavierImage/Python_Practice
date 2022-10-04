import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

visited = [[[0] * m for _ in range(n)] for _ in range(2)]

def bfs(r, c):
    k = 1
    queue = deque()
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    queue.append((k, r, c))
    visited[k][r][c] = 1
    while queue:
        k, r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<m:
                if visited[k][nr][nc] == 0 and board[nr][nc] == '0':
                    visited[k][nr][nc] = visited[k][r][c] + 1
                    queue.append((k, nr, nc))
        if k > 0:
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<n and 0<=nc<m:
                    if visited[k-1][nr][nc] == 0 and board[nr][nc] == '1':
                        visited[k-1][nr][nc] = visited[k][r][c] + 1
                        queue.append((k-1, nr, nc))

bfs(0, 0)
res = []
for i in range(len(visited)):
    if visited[i][n-1][m-1] != 0:
        res.append(visited[i][n-1][m-1])
if len(res) != 0:
    print(min(res))
else:
    print(-1)
  

            
