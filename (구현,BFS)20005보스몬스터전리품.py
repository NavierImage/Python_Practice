import sys
from collections import deque
n, m, p = map(int, sys.stdin.readline().rstrip().split())

arr = []
for i in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))

player_dict = {}
for i in range(p):
    player, dps = map(str, sys.stdin.readline().rstrip().split())
    dps = int(dps)
    player_dict[player] = dps 

HP = int(sys.stdin.readline().rstrip())

def bfs(arr, y, x):
    time = 0
    queue = deque()
    queue.append((y, x, time))
    visited = [[0] * m for i in range(n)]
    visited[y][x] = 1  
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    while queue:
        y, x, time = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if visited[ny][nx] == 0:
                    if arr[ny][nx] == "X":
                        continue
                    if arr[ny][nx] == "B":
                        return int(time + 1)
                    visited[ny][nx] = 1
                    queue.append((ny, nx, time+1))

ptob_time_dict = {}

for i in range(n):
    for j in range(m):
        if arr[i][j] in player_dict:
            time_taken = bfs(arr, i, j)
            ptob_time_dict[arr[i][j]] = time_taken

time_tick = 1
done_dict = {}
while True:
    for key, val in ptob_time_dict.items():
        if time_tick > val:
            HP -= player_dict[key]
            done_dict[key] = 1 
    if HP < 0:
        break 
    time_tick += 1

print(len(list(done_dict.keys())))

# time_list = []
# for key, val in ptob_time_dict.items():
#     time_list.append((key, val))
# time_list.sort(key=lambda x:-x[0])
# max_time = time_list[0][0]

# for 