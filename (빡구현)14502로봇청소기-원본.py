n, m = map(int, input().split())
#위 북 아래 남 왼 서 오른 동
y, x, d = map(int, input().split())
can = []
for i in range(n):
    temp = list(map(int, input().split()))
    can.append(temp)

dx = [1, -1, 0 , 0]
dy = [0, 0, 1, -1] #동서남북
spincnt = 0
cnt = 0
while(1):
    if can[y][x] != 2: #청소를 한칸 = 2 안한칸 = 0
        cnt += 1
    can[y][x] = 2
    nx = 0 #여기선 1인 칸을 지나갈수가 없으므로 임시변수없이 그냥 바로바로 칸이동시켜줘도됨
    ny = 0
    if spincnt == 4: #4번을 돌고나면 뒤에 비어있는지 안비어있는지 판단
        if d == 0:
            if can[y+1][x] == 1:
                break
            else:
                nx = x + dx[2]
                ny = y + dy[2]
                spincnt = 0
        elif d == 1:
            if can[y][x-1] == 1:
                break
            else:
                nx = x + dx[1]
                ny = y + dy[1]
                spincnt = 0
        elif d == 2:
            if can[y-1][x] == 1:
                break
            else:
                nx = x + dx[3]
                ny = y + dy[3]
                spincnt = 0
        elif d == 3:
            if can[y][x+1] == 1:
                break
            else:
                nx = x + dx[0]
                ny = y + dy[0]
                spincnt = 0
    else:    
        if d == 0: #북
            if can[y][x-1] == 1 or can[y][x-1] == 2: #막혀있거나 청소한칸으로는 이동안하고 회전만
                d = 3
                spincnt += 1
                continue
            else: #막혀있지않고 청소안된칸이면 이동
                d = 3
                nx = x + dx[1]
                ny = y + dy[1]
                spincnt = 0
        elif d == 1: #동
            if can[y-1][x] == 1 or can[y-1][x] == 2:
                d = 0
                spincnt += 1
                continue
            else:
                d = 0
                nx = x + dx[3]
                ny = y + dy[3]
                spincnt = 0
        elif d == 2: #남
            if can[y][x+1] == 1 or can[y][x+1] == 2:
                d = 1
                spincnt +=1
                continue
            else:
                d = 1
                nx = x + dx[0]
                ny = y + dy[0]
                spincnt = 0
        elif d == 3: #서
            if can[y+1][x] == 1 or can[y+1][x] == 2:
                d = 2
                spincnt += 1
                continue
            else:
                d = 2
                nx = x + dx[2]
                ny = y + dy[2]
                spincnt = 0
        
    x, y = nx, ny #임시변수 설정
    
print(cnt)