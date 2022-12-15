import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split())
arr = [[0] * n for _ in range(n)]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
fire_ball = []
for _ in range(m): 
    r, c, mi, si, di = map(int, sys.stdin.readline().rstrip().split())
    r -= 1; c -= 1
    fire_ball.append((r, c, mi, si, di))

for _ in range(k):
    mi_map = [[0] * n for _ in range(n)]
    si_map = [[0] * n for _ in range(n)]
    di_map = [[[] * 2 for _ in range(n)] for _ in range(n)]
    cnt_map = [[0] * n for _ in range(n)]
    
    for i, item in enumerate(fire_ball):
        y, x, mi, si, di = item
        ny = y + dy[di] * si
        nx = x + dx[di] * si
        if nx < 0:
            while nx < 0:
                nx += n
        elif nx >= n:
            while nx >= n:
                nx -= n
        if ny < 0:
            while ny < 0:
                ny += n
        elif ny >= n:
            while ny >= n:
                ny -= n
        
        mi_map[ny][nx] += mi
        si_map[ny][nx] += si
        di_map[ny][nx].append(di)
        cnt_map[ny][nx] += 1
    new_fire_ball = []
    
    for i in range(n):
        for j in range(n):
            if cnt_map[i][j] > 1:
                
                new_mi = mi_map[i][j]//5
                if new_mi < 1:
                    continue
                
                new_si = si_map[i][j]//cnt_map[i][j]
                std_di = di_map[i][j][0]%2
                even_di = [0, 2, 4, 6]
                odd_di = [1, 3, 5, 7]
                for d in range(1, len(di_map[i][j])):
                    if di_map[i][j][d]%2 != std_di:
                        next_di = odd_di[:]
                        break
                else:
                    next_di = even_di[:]
                for fb in range(len(next_di)):
                    new_fire_ball.append((i, j, new_mi, new_si, next_di[fb]))
            elif cnt_map[i][j] == 1:
                new_fire_ball.append((i, j, mi_map[i][j], si_map[i][j], di_map[i][j][0]))
    
    fire_ball = new_fire_ball[:]
    
ans = 0
for i in range(len(fire_ball)):
    r, c, mi, si, di = fire_ball[i]
    ans += mi
print(ans)
                
