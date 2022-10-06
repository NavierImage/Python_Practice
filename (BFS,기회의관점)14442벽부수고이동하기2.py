import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().rstrip().split())

board = []

for i in range(n):
    board.append(list(sys.stdin.readline().rstrip()))
visited = [[[0] * m for _ in range(n)] for _ in range(k+1)]
def bfs(k, r, c):
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    queue = deque()
    queue.append((k, r, c))
    visited[k][r][c] = 1
    while queue:
        k, r, c= queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<m:
                if visited[k][nr][nc] == 0 and board[nr][nc] == '0':
                    visited[k][nr][nc] = visited[k][r][c] + 1
                    queue.append((k, nr, nc))

                if k > 0 and visited[k-1][nr][nc] == 0 and board[nr][nc] == '1':
                    visited[k-1][nr][nc] = visited[k][r][c] + 1
                    queue.append((k-1, nr, nc))

bfs(k, 0, 0)
res = []
for i in range(k+1):
    a = visited[i][n-1][m-1]
    if a > 0:
        res.append(a)

if len(res) == 0:
    print(-1)
else:
    print(min(res))