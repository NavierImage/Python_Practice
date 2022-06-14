import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())

vill = []
for _ in range(n):
    vill.append(list(map(int, sys.stdin.readline().rstrip().split())))

vrs1 = deque() #바이러스 1담을거
vrs2 = deque() #바이러스 2담을거
for i in range(n):
    for j in range(m):
        if vill[i][j] == 1:
            vrs1.append((i, j))
        elif vill[i][j] == 2:
            vrs2.append((i, j))
cnt = [0, 0, 0] #이렇게 하면 시간 줄이기 가능
def bfs():
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    #temp로 끊어치기 bfs ㅋㅋ (bfs 두개 돌릴때 이렇게)
    while(1):
        temp1 = [] 
        while vrs1:
            r1, c1 = vrs1.popleft()
            for i in range(4):
                nr1 = r1 + dr[i]
                nc1 = c1 + dc[i]
                if nr1 < 0 or nc1 < 0 or nr1 >= n or nc1 >= m:
                    continue
                if vill[nr1][nc1] == 1 or vill[nr1][nc1]== -1 or vill[nr1][nc1]== 2 or vill[nr1][nc1] == 3:
                    continue
                if vill[nr1][nc1] == 0:
                    vill[nr1][nc1] = 1
                    cnt[0] += 1
                    temp1.append((nr1, nc1)) #vrs1에 안담고 temp1에 담기
        temp2 = []
        while vrs2:
            r2, c2 = vrs2.popleft()
            for i in range(4):
                nr2 = r2 + dr[i]
                nc2 = c2 + dc[i]
                if nr2 < 0 or nc2 < 0 or nr2 >= n or nc2 >= m:
                    continue
                if vill[nr2][nc2] == 2 or vill[nr2][nc2] == 3 or vill[nr2][nc2] == -1:
                    continue
                if vill[nr2][nc2] == 1 and (nr2, nc2) in temp1:
                    vill[nr2][nc2] = 3 #만약 1이고, temp에 있으면 방금전에 넣은것이므로 1과 2 동시에 가는거로 판정
                    temp1.pop(temp1.index((nr2, nc2))) #3이면 더이상 안퍼지므로 temp1에서 빼기
                    cnt[0] -= 1; cnt[2] += 1
                if vill[nr2][nc2] == 0:
                    vill[nr2][nc2] = 2
                    cnt[1] += 1
                    temp2.append((nr2, nc2)) #temp에 추가
        if len(temp2) > 0:
            for i in temp2:
                vrs2.append(i) #temp2에 담긴거있으면 이제 vrs2에 넣어주기

        if len(temp1) > 0:
            for i in temp1:
                vrs1.append(i) #temp1에 담긴게 있으면 이제 vrs1에 넣어주기
        
        if len(vrs1) == 0 and len(vrs2) == 0:
            break

bfs()
cnt[0] += 1
cnt[1] += 1
print(*cnt)
