import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
cheese = []
for _ in range(n):
    cheese.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
def bfs():
    queue = deque()
    queue.append((0, 0))
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    while queue:
        r, c = queue.popleft()
        for _ in range(4):
            nr = r + dr[_]
            nc = c + dc[_]
            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue
            if visited[nr][nc] == 1:
                continue
            if cheese[nr][nc] == 1: #바깥쪽탐색-> 1이면 큐에 넣지않음,방문처리는하고 0으로 변경(녹음)
                cheese[nr][nc] = 0
                visited[nr][nc] = 1
            else:
                queue.append((nr, nc))
                visited[nr][nc] = 1

cnt = 0
while(1):
    cnt += 1
    chcnt = 0
    
    for i in range(len(cheese)):
        for j in range(len(cheese[i])):
            if cheese[i][j] == 1:
                chcnt += 1       
    bfs()
    flag = 0
    for i in cheese:
        if 1 in i:
            break
    else:
        if chcnt > 0:
            print(cnt)
            print(chcnt)
            break
        else:
            print(0)
            print(0)
#https://www.acmicpc.net/problem/2636