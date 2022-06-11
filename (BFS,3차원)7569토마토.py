import sys
from collections import deque
m, n, h = map(int, sys.stdin.readline().rstrip().split())
volume = []
for _ in range(h):
    plane = []
    for __ in range(n):
        temp = list(map(int, sys.stdin.readline().rstrip().split()))
        plane.append(temp)
    volume.append(plane)

que = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if volume[i][j][k] == 1:
                que.append((i, j, k, 0)) 
#애초에 time이나 이동정보를 뒤에 하나 더넣어주면 visited배열 안만들고 가능
#예전 보다 많이 깔끔해졌다
def bfs():
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    mintime = 0
    while que:
        x, y, z, time = que.popleft() 
        #time이 현재걸리는 최소시간 보다 크면 더 이동을 했다는 것.
        #업데이트
        if time > mintime:
            mintime = time
        for _ in range(6):
            nx = x + dx[_]
            ny = y + dy[_]
            nz = z + dz[_]
            #상자 밖으로 나갈경우 continue
            if nx < 0 or ny < 0 or nz < 0 or nx >= h or ny >= n or nz >= m:
                continue
            #토마토가 들어있지 않은 칸을 만날 경우 continue
            if volume[nx][ny][nz] == -1:
                continue
            #조건에 맞는, 가야할 인접 칸을 만나면
            if volume[nx][ny][nz] == 0:
                #토마토를 익음 처리해주고, 걸린 시간 정보 + 1 해서 큐로 넣어줌
                volume[nx][ny][nz] = 1
                que.append((nx, ny, nz, time + 1))
    #BFS진행 후, 0으로 남아있는 칸이 있다면, flag =1 로 설정하여 -1출력될수 있게
    flag = 0
    for i in range(h):
        for j in range(n):
            if 0 in volume[i][j]:
                flag = 1
        if flag:
            break
    
    if flag: print(-1)
    else: print(mintime) # flag =0이라면 그냥 mintime 출력
bfs()
       