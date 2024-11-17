import sys 
from collections import deque 
w, h = map(int, sys.stdin.readline().rstrip().split())
n = int(sys.stdin.readline().rstrip())
arr = [[0] * w for _ in range(h)]

source_list = []
ans_list = []
for _ in range(n):
    cmd, c, r = sys.stdin.readline().rstrip().split()
    r = int(r); c = int(c)
    if cmd == "redstone_block":
        arr[r][c] = 1
        source_list.append((r, c))
    elif cmd == "redstone_dust":
        arr[r][c] = 2
    elif cmd == "redstone_lamp":
        arr[r][c] = 3 
        ans_list.append((r, c))

def bfs(y, x, visited):
    
    power = 15
    visited[y][x] = power
    queue = deque()
    
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    cnt = 0
    whatis = 1
    
    lampon_list = []
    queue.append((y, x, whatis, power))
    while queue:
        # for a in arr:
        #     print(a)
        # print()
        # for v in visited:
        #     print(v)
        # print()
        y, x, whatis, power = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<h and 0<=nx<w:
                pass 
            else:
                continue
            if visited[ny][nx] == 0:
                if arr[ny][nx] == 2:
                    if whatis == 1:
                        visited[ny][nx] = power
                        queue.append((ny, nx, arr[ny][nx], power))
                    elif whatis == 2:
                        if power - 1 == 0:
                            continue
                        visited[ny][nx] = power - 1
                        queue.append((ny, nx, arr[ny][nx], power - 1))
                elif arr[ny][nx] == 3:
                    if whatis == 1:
                        if power > visited[ny][nx]:
                            lampon_list.append((ny, nx))
                            visited[ny][nx] = power
                    elif whatis == 2:
                        if power - 1 == 0:
                            continue
                        else:
                            if power - 1 > visited[ny][nx]:
                                lampon_list.append((ny, nx))
                                visited[ny][nx] = power - 1
            else:
                if arr[ny][nx] == 2:
                    if whatis == 1:
                        if power > visited[ny][nx]:
                            visited[ny][nx] = power
                            queue.append((ny, nx, arr[ny][nx], power)) 
                    elif whatis == 2:
                        if power - 1 > visited[ny][nx]:
                            visited[ny][nx] = power - 1
                            queue.append((ny, nx, arr[ny][nx], power - 1))
                elif arr[ny][nx] == 3:
                    if whatis == 1:
                        if power > visited[ny][nx]: # 중복처리 못하게 걸어줘야...
                            lampon_list.append((ny, nx))
                            visited[ny][nx] = power
                    elif whatis == 2:
                        if power - 1 == 0:
                            continue
                        else:
                            if power - 1 > visited[ny][nx]:
                                lampon_list.append((ny, nx))
                                visited[ny][nx] = power - 1
    return lampon_list, visited

visited = [[0] * w for _ in range(h)]
rst = [] 
for co in source_list:
    y, x = co 
    temp_rst, visited = bfs(y, x, visited)
    rst = rst  + temp_rst 

# print(rst)
# rst = list(set(rst)) # 한 ramp 에서 시작한게 같은 정답이 잇을수도 있음 중복처리를안함...

rst.sort()
ans_list.sort()
if rst == ans_list and len(ans_list) != 0:
    print("success")
else:
    print("failed")