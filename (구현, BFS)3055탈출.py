import sys
from collections import deque

def bfs(y, x, water_list):
    queue = deque()
    queue.append((y, x))
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    visited = [[0] * m for _ in range(n)]
    visited[y][x] = 1
    idx = 0
    while True:
        idx += 1
        new_q = [] #이게 밖에 있어야... new_q에 각 ny, nx (ty, tx부분) 에서 4방향 탐색하고 물 없으면 그때 넣은 걸 보존가능
        if idx >= 3000: #문제의 제한범위 생각
            return "KAKTUS"
        while queue:
            temp = [] #ny, nx 에서 4방향 한번 더 탐색용
            y, x = queue.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<=ny<n and 0<=nx<m:
                    if visited[ny][nx] == 0 and arr[ny][nx] == '.':
                        temp.append((ny, nx))
                        
                    if arr[ny][nx] == 'D':
                        return visited[y][x]
            
            for idx, tmp in enumerate(temp):
                ty, tx = tmp[0], tmp[1]
                check = 0
                for i in range(4):
                    nty = ty +dy[i]
                    ntx = tx +dx[i]
                    if 0<=nty<n and 0<=ntx<m:
                        if arr[nty][ntx] == '*':
                            check = 1
                if check == 0:
                    new_q.append((ty, tx))
                    visited[ty][tx] = visited[y][x] + 1
        queue = deque(new_q) 
        #새로운 물 큐
        new_water_list = []
        for water in water_list:
            wy, wx = water
            for i in range(4):
                nwy = wy + dy[i]
                nwx = wx + dx[i]
                if 0<=nwy<n and 0<=nwx<m:
                    if arr[nwy][nwx] == '.':
                        arr[nwy][nwx] = '*'
                        new_water_list.append((nwy, nwx))
        
        water_list = new_water_list[:]

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))

water_list = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == '*':
            water_list.append((i, j))
        elif arr[i][j] == 'S':
            y, x = i, j
ans = bfs(y, x, water_list)
print(ans)
