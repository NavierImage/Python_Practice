import sys
from collections import deque
from itertools import product, permutations

height = 5
width = 5
maze_set = [[], [], [], [], []]
for _ in range(height):
    #회전된 배열 저장
    temp_2d = []
    for i in range(width):
        temp = list(map(int, sys.stdin.readline().rstrip().split()))
        temp_2d.append(temp)
    
    temp1 = []
    for i in range(width):
        tmp = []
        for j in range(width):
            tmp.append(temp_2d[i][j])
        temp1.append(tmp)
    maze_set[_].append(temp1)

    temp2 = []
    for j in range(width-1, -1, -1):
        tmp = []
        for i in range(width):
            tmp.append(temp_2d[i][j])
        temp2.append(tmp)
    maze_set[_].append(temp2)

    temp3 = []
    for i in range(width-1, -1, -1):
        tmp = []
        for j in range(width-1, -1, -1):
            tmp.append(temp_2d[i][j])
        temp3.append(tmp)
    maze_set[_].append(temp3)

    temp4 = []
    for j in range(width):
        tmp = []
        for i in range(width-1, -1, -1):
            tmp.append(temp_2d[i][j])
        temp4.append(tmp)
    maze_set[_].append(temp4)
    #회전 방향에 유의, 그냥 막 전치시키면안됨..
idx_rotate = [0, 1, 2, 3]
idx_stack = [0, 1, 2, 3, 4]

rep_per =  list(product(idx_rotate, repeat = 5))
comb = list(permutations(idx_stack, r = 5))
voxels = []

for i in range(len(comb)):
    a = comb[i][0]
    b = comb[i][1]
    c = comb[i][2]
    d = comb[i][3]
    e = comb[i][4]
    #몇번째 판(2차원 배열)인지 인덱싱
    for j in range(len(rep_per)):
        temp = []
        A = rep_per[j][0]
        B = rep_per[j][1]
        C = rep_per[j][2]
        D = rep_per[j][3]
        E = rep_per[j][4]
        #몇번째 회전된 것인지 인덱싱
        #ex)maze_set[0][1] -> 0번째 판, 1번째 회전된것
        temp.append(maze_set[a][A])
        temp.append(maze_set[b][B])
        temp.append(maze_set[c][C])
        temp.append(maze_set[d][D])
        temp.append(maze_set[e][E])
        voxels.append(temp)


def bfs(voxel, x, y, z):
    visited = []
    for i in range(5):
        visit = [[0] * 5 for _ in range(5)]
        visited.append(visit)
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    queue = deque()
    queue.append((x, y, z))
    visited[x][y][z] = 1
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and 0<= nz <5:
                if visited[nx][ny][nz] == 0 and voxel[nx][ny][nz] == 1:
                    queue.append((nx, ny, nz))
                    visited[nx][ny][nz] = visited[x][y][z] + 1
        
    return visited
res = []

for i in range(len(voxels)):
    visited = 0
    voxel = voxels[i]
    #모든 회전하는 경우를 고려하므로 그냥 서로 상반되는 꼭짓점만 검사하면됨.
    if voxel[0][0][0] == 0:
        continue
    else:
        visited = bfs(voxel, 0, 0, 0)
        
    if visited[4][4][4] == 0:
        continue 
    else:
        res.append(visited[4][4][4])

if len(res) == 0:
    print(-1)
else:
    print(min(res)-1)
#https://www.acmicpc.net/problem/16985