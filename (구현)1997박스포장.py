import sys
n, w, b = map(int, sys.stdin.readline().rstrip().split())

panel = []
arrheight = []
total_height = 0
for _ in range(n):
    h = int(sys.stdin.readline().rstrip())
    total_height += h
    arr = []
    for i in range(h):
        arr.append(list(sys.stdin.readline().rstrip()))
    panel.append(arr)



def find_below(arr):
    below_points = []
    row = len(arr[0])
    for j in range(row):
        for i in range(len(arr)-1, -1, -1):
            if arr[i][j] == 'X':
                below_points.append((i, j))
                break
    return below_points

def find_top(arr):
    top_points = []
    row = len(arr[0])
    for j in range(row):
        for i in range(len(arr)):
            if arr[i][j] == 'X':
                top_points.append((i, j))
                break
    if top_points == []:
        for j in range(len(arr[-1])):
            top_points.append((len(arr), j))

    return top_points

done_list = [0] * n
ans_list = []

t_box = [['.'] * w for _ in range(b)]
for asdf in range(10000):
    t_box = [['.'] * w for _ in range(b)]
    #오바하는 경우에도 그냥 덮어 씌우네...
    for _ in range(len(panel)):
        stacked = 0
        if done_list[_] == 1:
            continue
        
        
        b_p = find_below(panel[_])
        t_p = find_top(t_box)
        
        dists = []
        check = 0
        for i in range(len(b_p)):
            y1, x1 = b_p[i]
            y2, x2 = t_p[i]
            if y2-y1 <= 0:
                check = 1
                for i in range(len(t_box)-1, -1, -1):
                    if "X" in t_box[i]:
                        stacked += 1
                    else: break
            if check:
                break
            dists.append(y2-y1)
        if check:
            ans_list.append(stacked)
            break

        move_down = min(dists)
        if move_down <= 0:
            break
        for i in range(len(panel[_])):
            for j in range(len(panel[_][i])):
                if panel[_][i][j] == 'X':
                    t_box[i+move_down-1][j] = panel[_][i][j]

        done_list[_] = 1
        # for t in t_box:
            # print(t)
        # print()    
    if done_list == [1] * n:
        break

for i in range(len(t_box)-1, -1, -1):
    if "X" in t_box[i]:
        stacked += 1
    else: break    
ans_list.append(stacked)


print(*ans_list)
