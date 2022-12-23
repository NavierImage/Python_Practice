import sys
import copy
from collections import deque
n, q = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(2**n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

act = list(map(int, sys.stdin.readline().rstrip().split()))

    
def bfs2(i, j):
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    queue = deque()
    queue.append((i, j))
    v2[i][j] = True
    cnt = 1
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=nx<(2**n) and 0<=ny<(2**n):
                if v2[ny][nx] == False and arr[ny][nx] != 0:
                    v2[ny][nx] = True
                    queue.append((ny, nx))
                    cnt += 1
    return cnt 
    
    
for _, act_num in enumerate(act):
    narr = [[0] * (2**n) for _ in range(2**n)]
    visited = [[False]*(2**n) for _ in range(2**n)]
    v2 = [[False]*(2**n) for _ in range(2**n)]
    for idx in range(0, 2**n, 2**act_num):
        for jdx in range(0, 2**n, 2**act_num):
            tmparr = [[0] * (2**act_num) for _ in range(2**act_num)]
            tmp2arr = [[0] * (2**act_num) for _ in range(2**act_num)]
            for i in range(idx, idx + 2**act_num):
                for j in range(jdx, jdx + 2**act_num):
                    tmparr[i-idx][j-jdx] = arr[i][j]
            for i in range(len(tmparr)):
                for j in range(len(tmparr[i])):
                    tmp2arr[j][len(tmparr)-1-i] = tmparr[i][j]

            for i in range(idx, idx + 2**act_num):
                for j in range(jdx, jdx + 2**act_num):
                    narr[i][j] = tmp2arr[i-idx][j-jdx]
    arr = copy.deepcopy(narr)
    movemap = [[0] * (2**n) for _ in range(2**n)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            cnt = 0
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                if 0<=ny<(2**n) and 0<=nx<(2**n):
                    if arr[ny][nx] != 0:
                        cnt += 1
            if cnt < 3:
                movemap[i][j] -= 1

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] += movemap[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0

cnt_list = []
for i in range(2**n):
    for j in range(2**n):
        if v2[i][j] == False and arr[i][j] != 0:
            cnt_list.append(bfs2(i, j))
        else:
            continue
ans = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        ans += arr[i][j]
print(ans)
try:print(max(cnt_list))
except:print(0)