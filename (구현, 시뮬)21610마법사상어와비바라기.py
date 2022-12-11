import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
direction = []
move = []

dy_li = [0, -1, -1, -1, 0, 1, 1, 1]
dx_li = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(m):
    di, si = map(int, sys.stdin.readline().rstrip().split())
    direction.append(di-1)
    move.append(si)

for turn in range(m):
    if turn == 0:
        clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

    #구름 이동 부분
    for i in range(len(clouds)):
        cy, cx = clouds[i] 
        dy = dy_li[direction[turn]]
        dx = dx_li[direction[turn]]
        dy *= move[turn]
        dx *= move[turn]
        
        ny = cy + dy
        nx = cx + dx   

        if ny < 0:
            while ny < 0:
                ny += n
        elif ny >= n:
            while ny > n-1:
                ny -= n
            
        if nx < 0:
            while nx < 0:
                nx += n
        elif nx >= n:
            while nx > n-1:
                nx -= n
        
        clouds[i] = (ny, nx)
    #이동된 구름 위치에 물 내려주기
    for i in range(len(clouds)):
        arr[clouds[i][0]][clouds[i][1]] += 1

    #물이 있는 대각선 따라 추가할 물 계산할 map
    diff_map = [[0] * n for _ in range(n)]
    
    #추가할 물 대각선 for loop 돌면서 계산
    for i in range(len(clouds)):
        cy, cx = clouds[i]
        for d in range(1, 8, 2):
            ny = cy + dy_li[d]
            nx = cx + dx_li[d]
            if 0<=ny<n and 0<=nx<n:
                if arr[ny][nx] > 0:
                    diff_map[cy][cx] += 1

    #구름 위치에서만 추가할 물 계산하므로 구름 좌표만 돌면서 물 추가
    for i in range(len(clouds)):
        cy, cx = clouds[i]
        arr[cy][cx] += diff_map[cy][cx]
    
    #현재 구름 위치 제외한 2 이상인 물인곳만 구름 설정해줌 (2 빼주고..)
    new_clouds = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and (i, j) not in clouds:
                new_clouds.append((i, j))
                arr[i][j] -= 2
    clouds = new_clouds[:]


    
#for i in arr:
#    print(i)
#print(clouds)
s = 0
for i in arr:
    s += sum(i)
print(s)