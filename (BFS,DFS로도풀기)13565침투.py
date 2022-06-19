import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

visited = [[0]*m for _ in range(n)]
q = deque()
for i in range(1):
    for j in range(m):
        if board[i][j] == '0':
            q.append((i, j))
            visited[i][j] = 1

#기본적 bfs문제
def bfs():
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue
            if board[nr][nc] == '1':
                continue
            if visited[nr][nc] == 1:
                continue
            visited[nr][nc] = 1
            q.append((nr, nc))
bfs()

flag = 0 
for i in range(len(visited[len(visited)-1])):
    if visited[len(visited)-1][i] == 1:
        print('YES')
        flag = 1
        break

if flag == 0:
    print('NO')
#https://www.acmicpc.net/problem/13565