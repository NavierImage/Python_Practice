import sys
from collections import deque

n = 12
m = 6
field = []
for _ in range(n):
    field.append(list(sys.stdin.readline().rstrip()))

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited = [[0] * m for _ in range(n)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    color = field[r][c]
    color_list = []
    while queue:
        r, c = queue.popleft()
        for i in range(len(dr)):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<= nr < n and 0<= nc < m:
                if field[nr][nc] == color and visited[nr][nc] == 0:
                    color_list.append((nr, nc))
                    queue.append((nr, nc))
                    visited[nr][nc] = 1

    if len(color_list) >= 4:
        for _ in range(len(color_list)):
            a, b = color_list[_]
            field[a][b] = '.'
        return 1
    else:
        return 0

cnt = 0

didit = 1
while didit != 0:
    didit = 0 
    #탐색
    for i in range(n):
        for j in range(m):
            if field[i][j] != '.':
                flag = bfs(i, j)
                if flag == 1:
                    didit = 1
    if didit == 1:
        cnt += 1
    else:
        break
    
    #밑으로 떨어지는 것 구현 #정렬 아이디어
    for v in range(m):
        temp = []
        for u in range(n):
            temp.append(field[u][v])
        
        #버블 정렬, '.'는 올리고(인덱스 감소), 문자는 내리고(인덱스 증가)
        for ii in range(len(temp)):
            for jj in range(len(temp)-1):
                if temp[jj] != '.' and temp[jj+1] == '.':
                    temp[jj], temp[jj+1] = temp[jj+1], temp[jj]

                      
        for uu in range(n):
            field[uu][v] = temp[uu]
  
print(cnt)                