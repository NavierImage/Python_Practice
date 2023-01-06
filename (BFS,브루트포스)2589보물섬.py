import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))


def bfs(y, x):
    visited = [[0] * m for _ in range(n)]
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1
    dist_list = [1] #default distance
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if visited[ny][nx] == 0 and arr[ny][nx] == 'L':
                    visited[ny][nx] = visited[y][x] + 1
                    dist_list.append(visited[ny][nx])
                    queue.append((ny, nx))
    
    return max(dist_list)-1 #one move -> hour##12## -> ##01##

ans_list = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            ans_list.append(bfs(i, j))
print(max(ans_list))
