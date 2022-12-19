import sys
from collections import deque
n, m, fuel = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
iny, inx = map(int, sys.stdin.readline().rstrip().split())
iny-=1;inx-=1
man_dict = {}
for _ in range(m):
    dpt_y, dpt_x, arv_y, arv_x = map(int, sys.stdin.readline().rstrip().split())
    dpt_y -=1; dpt_x -= 1; arv_y -= 1; arv_x -= 1
    man_dict[(dpt_y, dpt_x)] = (arv_y, arv_x)

def bfs_find_man(y, x):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    queue = deque()
    visited = [[0] * n for _ in range(n)]
    y1 = y; x1 = x
    queue.append((y, x))
    
    visited[y][x] = 1
    dist_list = []
    ### 데려다 놓은 자리에 바로 승객있는 경우 ###
    if (y, x) in man_dict.keys():
        dist_list.append((0, y, x))
        return dist_list[0]

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<n:
                if visited[ny][nx] == 0 and arr[ny][nx] != 1:
                    visited[ny][nx] = visited[y][x] + 1
                    if (ny, nx) in man_dict.keys():
                        dist_list.append((visited[y][x], ny, nx))
                    queue.append((ny, nx))
    dist_list.sort(key=lambda x: (x[0], x[1], x[2]))
    
    try:return dist_list[0]
    except:return (-1, -1, -1)

def bfs_destination(y, x, start_y, start_x):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    queue = deque()
    visited = [[0] * n for _ in range(n)]
    y1 = y; x1 = x
    queue.append((y, x))
    visited[y][x] = 1
    dst_y, dst_x = man_dict[(start_y, start_x)]
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<n:
                if visited[ny][nx] == 0 and arr[ny][nx] != 1:
                    if (ny, nx) == (dst_y, dst_x):
                        man_dict.pop((start_y, start_x))
                        return (visited[y][x], ny, nx)
                    else:
                        visited[ny][nx] = visited[y][x] + 1
                        queue.append((ny, nx))
    return (-1, -1, -1)

for _ in range(m):
    d_to_man, yy, xx = bfs_find_man(iny, inx)
    if (d_to_man, yy, xx) == (-1,-1,-1): #승객 못태우러 간 경우
        print(-1)
        break
    fuel -= d_to_man
    d_to_dest, new_iny, new_inx = bfs_destination(yy, xx, yy, xx)
    if (d_to_dest, new_iny, new_inx) == (-1, -1, -1): #목적지로 못가는 경우
        print(-1)
        break
    fuel -= d_to_dest
    if fuel < 0:
        print(-1)
        break
    iny, inx = new_iny, new_inx
    fuel += 2*d_to_dest

if fuel >= 0 and (d_to_man, yy, xx) != (-1, -1, -1) and (d_to_dest, new_iny, new_inx) != (-1, -1, -1):
    print(fuel)
else:
    pass
    
    
