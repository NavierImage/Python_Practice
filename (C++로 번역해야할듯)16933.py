import sys
from collections import deque
n, m, k = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))
    
#c++...
def bfs(k, x, y):
    day = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((k, x, y, day))
    visited = [[[[0] * 2 for _ in range(m)] for _ in range(n)] for _ in range(k+1)]
    visited[k][x][y][day] = 1
    while queue:
        k, x, y, day = queue.popleft()
        if x == n-1 and y==m-1:
            return visited[k][x][y][day]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if day == 1:
                    if visited[k][nx][ny][day-1] == 0:
                        if arr[nx][ny] == '0':
                            visited[k][nx][ny][day-1] = visited[k][x][y][day] + 1
                            queue.append((k, nx, ny, day-1))
                    if k > 0 and arr[nx][ny] == '1':
                        if visited[k-1][nx][ny][day-1] == 0:
                            visited[k-1][nx][ny][day-1] = visited[k][x][y][day] + 1
                            queue.append((k-1, nx, ny, day-1))
                elif day == 0:
                    if visited[k][nx][ny][day+1] == 0:
                        if arr[nx][ny] == '0':
                            visited[k][nx][ny][day+1] = visited[k][x][y][day] + 1
                            queue.append((k, nx, ny, day+1))

                        if arr[nx][ny] == '1' and visited[k][x][y][day+1] == 0:
                            visited[k][x][y][day+1] = visited[k][x][y][day] + 1
                            queue.append((k, x, y, day+1))
    return -1

v = bfs(k, 0, 0)
if v==0:
    print(-1)
else:print(v)