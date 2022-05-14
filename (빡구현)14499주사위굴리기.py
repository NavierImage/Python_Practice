n, m, y, x, k = map(int, input().split())
maap = []
for i in range(n):
    temp = list(map(int, input().split()))
    maap.append(temp)

cmd = list(map(int, input().split()))
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1] #동서북남
dice_y = [0, 0, 0] 
dice_x = [0, 0, 0]
result = []
for i, t in enumerate(cmd):
    nx = 0
    ny = 0
    east = 0
    west = 0
    north = 0 
    south = 0
    if t == 1: #동
        nx = x + dx[0]
        ny = y + dy[0]
        east = 1
    elif t == 2: #서
        nx = x + dx[1]
        ny = y + dy[1]
        west = 1
    elif t == 3: #북
        nx = x + dx[2]
        ny = y + dy[2]
        north = 1
    elif t == 4: #남
        nx = x + dx[3]
        ny = y + dy[3]
        south = 1
    else:
        pass

    if nx >= m or ny >= n or nx < 0 or ny < 0:
        nx = 0
        ny = 0
        continue #기본적인 이동과 맵밖으로 나가면 이동 무시하는거... 여기까진 쉬웠음..ㅜㅜ
    else: #주사위구현부분...
        x = nx
        y = ny
        flag = 0
        if south == 1:
            if maap[y][x] == 0:
                maap[y][x] = dice_y[2] #인덱스 1이 땅에 깔리는걸로 설정해놓은거라 분기문 들어오자마자 인덱스 2를 체크하면 그게 곧 땅에 깔릴거임
                flag = 1 #만약 지도칸이 0이면.. flag 세우고 지도칸을 0으로 만들지 않음
            else:   
                dice_y[2] = maap[y][x]
            result.append(dice_y[0]) #주사위 위를 저장을시키고
            dice_y.pop(0) #앞을 삭제!
            dice_y.append(0) #비효율적인 부분이나 일단 이렇게 햇음
            dice_y[2] = result[len(result)-2] #위에 있던건 다시 뒤로 가서 순환하게됨
            dice_x[1] = maap[y][x]

        elif north == 1:
            dice_y.reverse()
            if maap[y][x] == 0:
                maap[y][x] = dice_y[2]
                flag = 1
            else:   
                dice_y[2] = maap[y][x]
            result.append(dice_y[0])
            dice_y.pop(0)
            dice_y.append(0)
            dice_y[2] = result[len(result)-2]
            dice_x[1] = maap[y][x]
            dice_y.reverse()
        elif east == 1:
            if maap[y][x] == 0:
                maap[y][x] = dice_x[2]
                flag = 1
            else:   
                dice_x[2] = maap[y][x]
            dice_x[2] = maap[y][x]
            result.append(dice_x[0])
            dice_x.pop(0)
            dice_x.append(0)
            dice_x[2] = result[len(result)-2]
            dice_y[1] = maap[y][x]
        elif west == 1:
            dice_x.reverse()
            if maap[y][x] == 0:
                maap[y][x] = dice_x[2]
                flag = 1
            else:   
                dice_x[2] = maap[y][x]
            result.append(dice_x[0])
            dice_x.pop(0)
            dice_x.append(0) 
            dice_x[2] = result[len(result)-2]
            dice_y[1] = maap[y][x]
            dice_x.reverse()
        if flag == 0:
            maap[y][x] = 0   #flag안세워졌으면 지나는 칸은 0으로     

if len(result) == 0:
    pass
else:
    for i in result:
        print(i)       
