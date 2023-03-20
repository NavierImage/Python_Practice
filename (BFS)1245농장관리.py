import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
done_visited = [[0] * m for _ in range(n)]
def bfs1(y, x):
    visited = [[0] * m for _ in range(n)]
    queue = deque()
    dy = [1, -1, 0, 0, 1, 1, -1, -1]
    dx = [0, 0, 1, -1, 1, -1, -1, 1]
    queue.append((y, x))
    visited[y][x] = 1
    no_flag = 0
    done_list = [(y,x)] #이거에 일단 되면 저장.. no_flag 안세우면 이거 반복문돌려서 done_visit 방문처리!!!
    while queue:
        y, x = queue.popleft()
        if done_visited[y][x] == 1:
            no_flag = 1
            break
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if visited[ny][nx] == 0: 
                    if arr[ny][nx] < arr[y][x]:
                        pass
                    elif arr[ny][nx] == arr[y][x]:
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
                        done_list.append((y, x))
                        # coord_queue.append((ny, nx))
                    elif arr[ny][nx] > arr[y][x]:
                        no_flag = 1
                        break
                
        if no_flag:
            break
    if no_flag:
        return -1
    else:
        for i in range(len(done_list)):
            y, x = done_list[i]
            done_visited[y][x] = 1
        return 1

cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            ans = bfs1(i, j)
            if ans == 1:
                cnt += 1
     
print(cnt)
                