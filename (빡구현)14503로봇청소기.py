#임시 x, y를 쓰지않은 버전 #최대한 줄일거 줄인 풀이
n, m = map(int, input().split())
y, x, d = map(int, input().split())
can = []
for i in range(n):
    temp = list(map(int, input().split()))
    can.append(temp)
dx = [1, -1, 0 , 0]
dy = [0, 0, 1, -1] 
spincnt = 0
cnt = 0
while(1):
    if can[y][x] != 2:
        cnt += 1
    can[y][x] = 2
    if spincnt == 4:
        if d == 0:
            if can[y+1][x] == 1:
                break
            else:
                y += dy[2]

        elif d == 1:
            if can[y][x-1] == 1:
                break
            else:
                x += dx[1]                
        elif d == 2:
            if can[y-1][x] == 1:
                break
            else:
                y += dy[3]               
        elif d == 3:
            if can[y][x+1] == 1:
                break
            else:
                x += dx[0]
                
    else:    
        if d == 0: #북
            if can[y][x-1] == 1 or can[y][x-1] == 2:
                d = 3
                spincnt += 1
                continue
            else:
                d = 3
                x += dx[1]
                
        elif d == 1: #동
            if can[y-1][x] == 1 or can[y-1][x] == 2:
                d = 0
                spincnt += 1
                continue
            else:
                d = 0
                y += dy[3]
                
        elif d == 2: #남
            if can[y][x+1] == 1 or can[y][x+1] == 2:
                d = 1
                spincnt +=1
                continue
            else:
                d = 1
                x += dx[0]
                
        elif d == 3: #서
            if can[y+1][x] == 1 or can[y+1][x] == 2:
                d = 2
                spincnt += 1
                continue
            else:
                d = 2
                y += dy[2]
                
    spincnt = 0
print(cnt)
#https://www.acmicpc.net/problem/14503
