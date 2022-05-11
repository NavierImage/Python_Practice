#1485정사각형
t = int(input())

rlt = []
for i in range(t):
    d = []
    vx = []
    vy = [] 
    for j in range(4):
        x, y = map(int, input().split())
        vx.append(x)
        vy.append(y)
    
    for u in range(4):
        for v in range(u, 4):
            dx = (vx[u] - vx[v])**2 
            dy = (vy[u] - vy[v])**2
            if (dx + dy) == 0:
                continue
            d.append((dx + dy)**(0.5))
    distance = set(d)
    cnt = 0
    det = []

    for u in distance:
        cnt = 0
        for v in d:
            if u == v:
                cnt += 1
        det.append(cnt)
    
    if det == [4, 2] or det == [2, 4]:
        rlt.append(1)
    else:
        rlt.append(0)
    
    print(det)
    print(d)

    #먼저 거리 다 똑같은지 확인한뒤,
    #같은 직선상에 세점 이상있다면 정사각형x

for i in rlt:
    print(i)
#https://www.acmicpc.net/problem/1485
