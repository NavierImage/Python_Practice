r, c, t = map(int, input().split())
room = []
for i in range(r):
    temp = list(map(int, input().split()))
    room.append(temp)

mach = []
for i in range(r):
    if -1 in room[i]:
        mach.append(i)

for rp in range(t):
    nroom = []
    for i in range(r):
        nroom.append(room[i][:])

    for i in range(r):
        for j in range(c):
            if room[i][j] != 0 and room[i][j] != -1:
                if i == 0 and j == 0:
                    nroom[0][1] += room[i][j] // 5
                    nroom[1][0] += room[i][j] // 5
                    nroom[0][0] -= 2*(room[i][j]//5)
                elif i == 0 and j == c-1:
                    nroom[0][c-2] += room[i][j]//5
                    nroom[1][c-1] += room[i][j]//5
                    nroom[0][c-1] -= 2*(room[i][j]//5)
                elif i == r-1 and j == 0:
                    nroom[r-2][0] += room[i][j]//5
                    nroom[r-1][1] += room[i][j]//5
                    nroom[r-1][0] -= 2*(room[i][j]//5)
                elif i == r-1 and j == c-1:
                    nroom[r-1][c-2] += room[i][j]//5
                    nroom[r-2][c-1] += room[i][j]//5
                    nroom[r-1][c-1] -= 2*(room[i][j]//5)
                
                elif i == mach[0] and j == 1:
                    nroom[i-1][j] += room[i][j]//5
                    nroom[i][j+1] += room[i][j]//5
                    nroom[i+1][j] += room[i][j]//5
                    nroom[i][j] -= 3*(room[i][j]//5)
                elif i == mach[1] and j == 1:
                    nroom[i-1][j] += room[i][j]//5
                    nroom[i][j+1] += room[i][j]//5
                    nroom[i+1][j] += room[i][j]//5
                    nroom[i][j] -= 3*(room[i][j]//5)
                elif j == 0 and (i+1) == mach[0]:
                    nroom[i-1][j] += room[i][j]//5
                    nroom[i][j+1] += room[i][j]//5
                    nroom[i][j] -= 2*(room[i][j]//5)
                elif j == 0 and (i-1) == mach[1]:
                    nroom[i+1][j] += room[i][j]//5
                    nroom[i][j+1] += room[i][j]//5
                    nroom[i][j] -= 2*(room[i][j]//5)
                    
                elif i == 0 and j > 0 and j < c-1: #윗변
                    nroom[i][j-1] += room[i][j]//5
                    nroom[i+1][j] += room[i][j]//5
                    nroom[i][j+1] += room[i][j]//5
                    nroom[i][j] -= 3*(room[i][j]//5)

                elif j == 0 and i > 0 and i < r-1: #왼변
                    nroom[i-1][j] += room[i][j]//5
                    nroom[i][j+1] += room[i][j]//5
                    nroom[i+1][j] += room[i][j]//5
                    nroom[i][j] -= 3*(room[i][j]//5)
                elif i == r-1 and j > 0 and j < c-1: #아랫변
                    nroom[i][j-1] += room[i][j]//5
                    nroom[i-1][j] += room[i][j]//5
                    nroom[i][j+1] += room[i][j]//5
                    nroom[i][j] -= 3*(room[i][j]//5)
                elif j == c-1 and i > 0 and i < r-1: #오른변
                    nroom[i+1][j] += room[i][j]//5
                    nroom[i][j-1] += room[i][j]//5
                    nroom[i-1][j] += room[i][j]//5
                    nroom[i][j] -= 3*(room[i][j]//5)
                
                else: #나머지 case
                    nroom[i-1][j] += room[i][j]//5
                    nroom[i][j-1] += room[i][j]//5
                    nroom[i+1][j] += room[i][j]//5
                    nroom[i][j+1] += room[i][j]//5
                    nroom[i][j] -= 4*(room[i][j]//5)
            else:
                pass
                    #확산 끝

    for u in range(mach[0]-1, 0, -1):
        nroom[u][0] = nroom[u-1][0]
        
    for v in range(c-1):
        nroom[0][v] = nroom[0][v+1]
        
    for u_ in range(mach[0]):
        nroom[u_][c-1] = nroom[u_+1][c-1]
    
    for v_ in range(c-1, 0, -1):
        if v_ != 1:
            nroom[mach[0]][v_] = nroom[mach[0]][v_-1]
        else:
            nroom[mach[0]][v_] = 0

    for ro in range(mach[1]+1, r-1):
        nroom[ro][0] = nroom[ro+1][0]
    
    for co in range(c-1):
        nroom[r-1][co] = nroom[r-1][co+1]
    
    for ro_ in range(r-1, mach[1], -1):
        nroom[ro_][c-1] = nroom[ro_-1][c-1]
    
    for co_ in range(c-1, 0, -1):
        if co_ != 1:
            nroom[mach[1]][co_] = nroom[mach[1]][co_-1]
        else:
            nroom[mach[1]][co_] = 0

    for p in range(r):
        room[p] = nroom[p][:]

sco = 0
for i in room:
    sco += sum(i)

print(sco+2)
