import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))
pr, pc = map(int, sys.stdin.readline().rstrip().split())
pr-=1; pc-=1

d_list = [0, 1, 2, 3]


def signal_sender(y, x, d):
    direction = [(-1, 0), (0, -1), (1, 0), (0, 1)] #Up left down right
    signal_cnt = 1
    st_y, st_x, st_d = y, x, d
    voy = 0
    visited = [[0] * m for _ in range(n)]
    while True:
        dy, dx = direction[d]
        ny, nx = y + dy, x + dx
        # print(d)
        # print(ny, nx)
        # for a in visited:
        #     print(a)
        # print()
        if (ny, nx, d) == (st_y, st_x, st_d):
            voy = 1
            break
        if 0<=ny<n and 0<=nx<m:
            # print(ny, nx)
            visited[ny][nx] = 1
            if arr[ny][nx] == "/":
                if d == 0:
                    d = 3
                    y, x = ny, nx
                elif d == 1:
                    d = 2
                    y, x = ny, nx 
                elif d == 2:
                    d = 1
                    y, x = ny, nx 
                elif d == 3:
                    d = 0
                    y, x = ny, nx 
            elif arr[ny][nx] == "\\":
                
                if d == 0:
                    d = 1
                    y, x = ny, nx 
                elif d == 1:
                    d = 0
                    y, x = ny, nx 
                elif d == 2:
                    d = 3
                    y, x = ny, nx
                elif d == 3:
                    d = 2
                    y, x = ny, nx
            elif arr[ny][nx] == ".":
                y, x = ny, nx
            elif arr[ny][nx] == "C":
                break
        else:
            break
        signal_cnt += 1

    return voy, signal_cnt

dir_dict = {0: "U", 1: "R", 2:"D", 3:"L"}
ans_list = []
for i, d in enumerate(d_list):
    dd = d
    if d == 1:
        dd = 3
    elif d == 3:
        dd = 1
    voy, sig_cnt = signal_sender(pr, pc, dd)
    ans_list.append((i, voy, sig_cnt))
ans_list.sort(key=lambda x:(-x[1], -x[2], x[0]))

sel_dir = ans_list[0][0]
signal_cnt =ans_list[0][2]

print(dir_dict[sel_dir])
if ans_list[0][1] == 1:
    print('Voyager')
else:
    print(signal_cnt)

