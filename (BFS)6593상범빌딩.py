import sys
from collections import deque

def bfs(z, r, c):
    queue = deque()
    queue.append((z, r, c))
    dz = [1, -1, 0, 0, 0, 0]
    dr = [0, 0, 1, -1, 0, 0]
    dc = [0, 0, 0, 0, 1, -1]
    visited = [[[0] * m for _ in range(n)] for __ in range(L)]
    
    visited[z][r][c] = 1
    find = 0

    while queue:
        z, r, c = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nz<L and 0<=nr<n and 0<=nc<m:
                if volume[nz][nr][nc] == '#':
                    continue
                elif visited[nz][nr][nc] != 0:
                    continue
                elif volume[nz][nr][nc] == '.' and visited[nz][nr][nc] == 0:
                    visited[nz][nr][nc] = visited[z][r][c] + 1
                    queue.append((nz, nr, nc))
                elif volume[nz][nr][nc] == 'E' and visited[nz][nr][nc] == 0:    
                    find = 1
                    visited[nz][nr][nc] = visited[z][r][c] + 1
                    return find, visited[nz][nr][nc]-1
    return find, 0

result_list = []
while True:         
    L, n, m = map(int, sys.stdin.readline().rstrip().split())
    if (L, n, m) == (0, 0, 0):
        break
    volume = []
    start_find = 0
    for k in range(L):
        floor = []
        for i in range(n+1):
            temp = list(sys.stdin.readline().rstrip())
            if temp == []:
                continue
            floor.append(temp)

        if start_find == 0:
            for i in range(n):
                for j in range(m):
                    if floor[i][j] == 'S':
                        st_z, st_r, st_c = k, i, j
                        start_find = 1

        volume.append(floor)
    find, val_min = bfs(st_z, st_r, st_c)
    
    if find == 0:
        result_list.append("Trapped!")
    else:
        result_list.append("Escaped in %d minute(s)." %val_min)

for i in range(len(result_list)):
    print(result_list[i])
