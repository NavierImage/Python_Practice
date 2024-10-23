import sys 
from collections import deque
n, k = map(int, sys.stdin.readline().rstrip().split())
arr = []
for i in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))
for i in range(n):
    for j in range(10):
        arr[i][j] = int(arr[i][j])

visited = [[0] * 10 for _ in range(10)]
def bfs(arr, visited, y, x, tgt_num):
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    queue = deque()
    visited[y][x] = 1
    queue.append((y, x))
    idx_list = [(y, x)]
    while queue:
        y, x = queue.popleft()
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0<= nx < 10:
                pass 
            else:
                continue
            if visited[ny][nx] == 1:
                continue 

            if arr[ny][nx] == tgt_num:
                queue.append((ny, nx))
                visited[ny][nx] = 1 
                idx_list.append((ny, nx))
    return idx_list, visited

def gravity(arr):
    for j in range(10):
        cnt = 0
        temp_list = []
        for i in range(n-1, -1, -1):
            if arr[i][j] != 0:
                cnt += 1 
                temp_list.append(arr[i][j]) # 있는거 다세고 
        
        tcnt = 0
        no_flag = 0
        for i in range(n-1, -1, -1):       #그것만큼 밑에서 다 채워버리고 나머지는 0
            if tcnt >= len(temp_list):
                arr[i][j] = 0
                no_flag = 1
            
            if no_flag == 0:
                arr[i][j] = temp_list[tcnt]
            tcnt += 1
            
    return arr

while True:
    visited = [[0] * 10 for i in range(n)]

    total_idx_list = []
    for i in range(n):
        for j in range(10):
            if arr[i][j] != 0 and visited[i][j] == 0:
                idx_list, visited = bfs(arr, visited, i, j, arr[i][j])
                if len(idx_list) >= k:
                    total_idx_list += idx_list
    
    if len(total_idx_list):               
        for idx in total_idx_list:
            y, x = idx
            arr[y][x] = 0
        arr = gravity(arr)
    else:
        break

for idx, a in enumerate(arr):
    for i in a:
        print(i, end="")
    if idx == len(arr)-1:
        pass 
    else:
        print()
