import sys 
from collections import deque
tc = int(sys.stdin.readline().rstrip())
col_dict = {
  "A": 0,
  "B": 1,
  "C": 2,
  "D": 3,
  "E": 4,
  "F": 5,
  "G": 6,
  "H": 7
}
row_dict = {
    "8": 0,
    "7": 1,
    "6": 2,
    "5": 3,
    "4": 4,
    "3": 5,
    "2": 6,
    "1": 7,
}
col_rev_dict = {v:k for k, v in col_dict.items()}
row_rev_dict = {v:k for k, v in row_dict.items()}
start_list = []
end_list = []
for i in range(tc):
    x1, y1, x2, y2 = sys.stdin.readline().rstrip().split()
    start_list.append((col_dict[x1], row_dict[y1]))
    end_list.append((col_dict[x2], row_dict[y2]))

arr = [[0] * 8 for _ in range(8)]
def bfs(y, x, ey, ex):
    visited = [[0] * 8 for _ in range(8)]
    queue = deque()
    visited[y][x] = 1 
    dy = [1, -1, 1, -1]
    dx = [1, 1, -1, -1]
    prod = [1, 2, 3, 4, 5, 6, 7]
    
    track = [(y, x)]
    queue.append((y, x, track))
    
    while queue:
        y, x, track = queue.popleft()

        if len(track) >= 6:
            continue
        for i in range(4):
            for p in prod:
                ny = y + dy[i] * p
                nx = x + dx[i] * p
                if 0<=ny<8 and 0<=nx<8:
                    if visited[ny][nx] == 0:
                        if (ny, nx) == (ey, ex):
                            return track + [(ny, nx)]
                        else:
                            visited[ny][nx] = 1
                            queue.append((ny, nx, track + [(ny, nx)]))
    return 0

for st, end in zip(start_list, end_list):
    x, y = st 
    ex, ey = end 
    if (x, y) == (ex, ey):
        print(0, col_rev_dict[x], row_rev_dict[y])
        continue
    rst = bfs(y, x, ey, ex)
    if rst == 0:
        print("Impossible")
    else:
        print(len(rst)-1, end="")
        for i, co in enumerate(rst):
            y, x = co 
            if i != len(rst)-1:
                print(f" {col_rev_dict[x]} {row_rev_dict[y]}", end="")
            else:
                print(f" {col_rev_dict[x]} {row_rev_dict[y]}")