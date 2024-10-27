import sys 
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for i in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))


visited = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]

def bfs(ry, rx, by, bx):
    cnt = 0
    queue = deque()
    visited[ry][rx][by][bx] = 1
    queue.append((ry, rx, by, bx, cnt))
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    while queue:
        ry, rx, by, bx, cnt = queue.popleft()
        for i in range(len(dy)):
            noflag = 0
            for j in range(10):
                rny = ry + dy[i] * j
                rnx = rx + dx[i] * j
                if 0<=rny<n and 0<=rnx<m:pass 
                else:
                    noflag = 1
                    break

                if arr[rny][rnx] == "#":
                    if i == 0:
                        rny -= 1
                    elif i == 1:
                        rny += 1
                    elif i == 2:
                        rnx -= 1
                    elif i == 3:
                        rnx += 1
                    break 
                elif arr[rny][rnx] == "O":
                    break
            if noflag:
                continue
            for j in range(10):
                bny = by + dy[i] * j
                bnx = bx + dx[i] * j
                # print(bny, bnx)
                if 0<=bny<n and 0<=bnx<m:pass 
                else:
                    noflag = 1
                    break

                if arr[bny][bnx] == "#":
                    if i == 0:
                        bny -= 1
                    elif i == 1:
                        bny += 1
                    elif i == 2:
                        bnx -= 1
                    elif i == 3:
                        bnx += 1
                    break
                elif arr[bny][bnx] == "O":
                    noflag=1
                    break
            if noflag:
                continue

            if (bny, bnx) == (rny, rnx): #겹칠때... 더많이 움직인 구슬이 뒤에 있어야함 (뒤에있었단 소리이므로)
                b_move_cnt = abs(bny - by) + abs(bnx - bx)
                r_move_cnt = abs(rny - ry) + abs(rnx - rx)
                
                if b_move_cnt > r_move_cnt:
                    bny += dy[i] * (-1)
                    bnx += dx[i] * (-1)
                elif r_move_cnt > b_move_cnt:
                    rny += dy[i] * (-1)
                    rnx += dx[i] * (-1)
            
            if arr[bny][bnx] == "O":
                continue 
            if arr[rny][rnx] == "O":
                return cnt+1
            
            if visited[rny][rnx][bny][bnx] == 0:
                
                visited[rny][rnx][bny][bnx] = 1
                queue.append((rny, rnx, bny, bnx, cnt+1))
    return -1

for i in range(n):
    for j in range(m):
        if arr[i][j] =="B":
            by, bx = i, j
        elif arr[i][j] == "R":
            ry, rx = i, j
what = bfs(ry, rx, by, bx)
# print(what)
if what<=10:
    print(what)
else:
    print(-1)

# 반례
# 10 10
# ##########
# #RB....#.#
# #..#.....#
# #........#
# #.O......#
# #...#....#
# #........#
# #........#
# #.......##
# ##########