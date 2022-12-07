import sys
import copy
from collections import deque

arr = []
n = 8
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))

#8번만 버티면 되는 거로 수정하면됨
#일단 3차원으로 모든 벽의 이동 맵 만들어 놓음
#가만히 8번 존버하는것도 고려해서 넉넉하게 25개로(실제론 16개면될듯)
arrs = []
for i in range(25):
    arrs.append(copy.deepcopy(arr))
    arr.insert(0, ['.'] * 8)
    arr.pop(-1)


def bfs(y=7, x=0, z = -1):
    queue = deque()
    dy = [0, 0, 0, 1, -1, 1, 1, -1, -1]
    dx = [0, 1, -1, 0, 0, 1, -1, 1, -1]
    
    queue.append((z, y, x))
    #사람이 이동후, 벽이 이동
    #벽이 이동하는건, z가 한칸(3차원에서 z축 하나 이동하면 벽이 이동된거)
    #큐에서 사람 위치꺼내고, z이동 시켜줌
    #만약 꺼낸 위치에 '#'이면 바로 생략
    while queue:
        z, y, x = queue.popleft()
        z += 1
        if z >= 25:
            break
        if arrs[z][y][x] == '#':
            continue
        
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=ny<n and 0<=nx<n:
                if arrs[z][ny][nx] == '.':
                    if (ny, nx) == (0, 7):
                        return 1
                    queue.append((z, ny, nx))
        
    return 0
print(bfs())