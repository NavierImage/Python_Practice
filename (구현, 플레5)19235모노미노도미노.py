import sys
n = int(sys.stdin.readline().rstrip())
cmd = []
for _ in range(n):
    t, x, y = map(int, sys.stdin.readline().rstrip().split())
    cmd.append((t, x, y))
r_arr = [[0] * 4 for _ in range(4)]
b_arr = [[0] * 4 for _ in range(6)]
g_arr = [[0] * 4 for _ in range(6)]

score = 0
for idx in range(n):
    t, x, y = cmd[idx]
    #blue board
    ######################보드에 투입########################
    if t == 1:
        for j in range(6):
            if b_arr[j][x] != 0:
                b_arr[j-1][x] = 1
                break
            if j == 5:
                b_arr[j][x] = 1
    elif t == 2:
        for j in range(5):
            if b_arr[j+1][x] != 0:
                b_arr[j-1][x] = 2
                b_arr[j][x] = 2
                break
            if j+1 == 5:
                b_arr[j+1][x]= 2
                b_arr[j][x] = 2
    elif t == 3:
        for j in range(5):
            f = 0
            for i in range(x, x+2):
                if b_arr[j+1][i] != 0:
                    b_arr[j][x] = 3
                    b_arr[j][x+1] = 3
                    f = 1
                    break
            if f: break
            if j + 1 == 5:
                b_arr[j+1][x+1] = 3
                b_arr[j+1][x] = 3
    ###########################################################################

    #########################중력 구현 및 4개 만족된 칸 삭제#############################        
    for shit in range(10):
        for i in range(4, -1, -1):
            for j in range(4):
                if b_arr[i][j] == 3:
                    q = j
                    nq = [0, 1, 2, 3]
                    
                    three_union_list = []
                    for dd in range(len(nq)):
                        if 0<= nq[dd] < 4:
                            if b_arr[i][nq[dd]] == 3:
                                three_union_list.append((i, nq[dd]))

                    if len(three_union_list) == 4:
                        if j == 0 or j == 1:
                            three_union_list = [(i, 0), (i, 1)]
                        elif j == 2 or j == 3:
                            three_union_list = [(i, 2), (i, 3)]
                    elif len(three_union_list) == 2:
                        pass

                    if len(three_union_list) == 2:
                        r = i
                        while True:
                            if 0<=r+1<6 and b_arr[r+1][three_union_list[0][1]] == 0 and b_arr[r+1][three_union_list[1][1]] == 0:
                                b_arr[r+1][three_union_list[0][1]] = b_arr[r][three_union_list[0][1]]
                                b_arr[r][three_union_list[0][1]] = 0
                                b_arr[r+1][three_union_list[1][1]] = b_arr[r][three_union_list[1][1]]
                                b_arr[r][three_union_list[1][1]] = 0
                                r += 1
                            else:
                                break
                    elif len(three_union_list) == 1:
                        r = i
                        while True:
                            if 0<=r+1<6 and b_arr[r+1][three_union_list[0][1]] == 0:
                                b_arr[r+1][three_union_list[0][1]] = b_arr[r][three_union_list[0][1]]
                                b_arr[r][three_union_list[0][1]] = 0
                                r += 1
                            else:
                                break
                            
                elif b_arr[i][j] == 2:
                    r = i
                    while True:
                        if 0<=r+1<6 and b_arr[r+1][j] == 0:
                            b_arr[r+1][j] = b_arr[r][j]
                            b_arr[r][j] = 0
                            r += 1
                        else:
                            break
                        
                elif b_arr[i][j] == 1:
                    r = i
                    while True:
                        if 0<=r+1<6 and b_arr[r+1][j] == 0:
                            b_arr[r+1][j] = b_arr[r][j]
                            b_arr[r][j] = 0
                            r += 1
                        else:
                            break
        del_indices = []
        for j in range(2, 6):
            bcnt = 0
            for i in range(4):
                if b_arr[j][i] != 0:
                    bcnt += 1
            if bcnt == 4:
                del_indices.append(j)
        for i in range(len(del_indices)):
            score += 1
            b_arr.pop(del_indices[i])
            b_arr.insert(0, [0, 0, 0, 0])   
    ########################################################################################

    #################################옅은 칸 체크후 블럭 존재시 맨 밑 부터 삭제############################################
    b_check = 0
    for j in range(2):
        for i in range(4):
            if b_arr[j][i] != 0:
                b_check += 1
                break

    for i in range(b_check):
        b_arr.pop(-1)
        b_arr.insert(0, [0, 0, 0, 0])
    #########################################################################################               

    #green board - 위와 같다.. 같은거는 같게 해줘야.............. ㅜ
    if t == 1:
        for i in range(6):
            if g_arr[i][y] != 0:
                g_arr[i-1][y] = 1
                break
            if i == 5:
                g_arr[i][y] = 1
    
    elif t == 2:
        for i in range(5):
            f = 0
            for j in range(y, y+2):
                if g_arr[i+1][j] != 0:
                    g_arr[i][y] = 2
                    g_arr[i][y+1] = 2
                    f = 1
                    break
            if f: break
            if i + 1 == 5:
                g_arr[i+1][y] = 2
                g_arr[i+1][y+1] = 2
            

    elif t == 3:
        for i in range(5):
            if g_arr[i+1][y] != 0:
                g_arr[i-1][y] = 3
                g_arr[i][y] = 3
                break
            if i+1 == 5:
                g_arr[i+1][y] = 3
                g_arr[i][y] = 3

    for shit in range(10):
        for i in range(4, -1, -1):
            for j in range(4):
                if g_arr[i][j] == 2:
                    q = j
                    nq = [0, 1, 2, 3]

                    two_union_list = []
                    for dd in range(len(nq)):
                        if 0<= nq[dd] < 4:
                            if g_arr[i][nq[dd]] == 2:

                                two_union_list.append((i, nq[dd]))
                    if len(two_union_list) == 4:
                        if j == 0 or j == 1:
                            two_union_list = [(i, 0), (i, 1)]
                        elif j == 2 or j == 3:
                            two_union_list = [(i, 2), (i, 3)]
                    elif len(two_union_list) == 2 or len(two_union_list) == 1:
                        pass

                    if len(two_union_list) == 2:
                        r = i
                        while True:
                            if 0<=r+1<6 and g_arr[r+1][two_union_list[0][1]] == 0 and g_arr[r+1][two_union_list[1][1]] == 0:
                                g_arr[r+1][two_union_list[0][1]] = g_arr[r][two_union_list[0][1]]
                                g_arr[r][two_union_list[0][1]] = 0
                                g_arr[r+1][two_union_list[1][1]] = g_arr[r][two_union_list[1][1]]
                                g_arr[r][two_union_list[1][1]] = 0
                                r += 1
                            else:
                                break
                    elif len(two_union_list) == 1:
                        r = i
                        while True:
                            if 0<=r+1<6 and g_arr[r+1][two_union_list[0][1]] == 0:
                                g_arr[r+1][two_union_list[0][1]] = g_arr[r][two_union_list[0][1]]
                                g_arr[r][two_union_list[0][1]] = 0
                                r += 1
                            else:
                                break

                elif g_arr[i][j] == 3:
                    r = i
                    while True:
                        if 0<=r+1<6 and g_arr[r+1][j] == 0:
                            g_arr[r+1][j] = g_arr[r][j]
                            g_arr[r][j] = 0
                            r += 1
                        else:
                            break

                elif g_arr[i][j] == 1:
                    r = i
                    while True:
                        if 0<=r+1<6 and g_arr[r+1][j] == 0:
                            g_arr[r+1][j] = g_arr[r][j]
                            g_arr[r][j] = 0
                            r += 1
                        else:
                            break

        del_indices = []
        for i in range(2, 6):
            gcnt = 0
            for j in range(4):
                if g_arr[i][j] != 0:
                    gcnt += 1
            if gcnt == 4:
                del_indices.append(i)
        for i in range(len(del_indices)):
            score += 1
            g_arr.pop(del_indices[i])
            g_arr.insert(0, [0, 0, 0, 0]) 

    g_check = 0
    for i in range(2):
        for j in range(4):
            if g_arr[i][j] != 0:
                g_check += 1
                break
    for i in range(g_check):
        g_arr.pop(-1)
        g_arr.insert(0, [0, 0, 0, 0])

counts = 0
for i in range(6):
    for j in range(4):
        if b_arr[i][j] != 0:
            counts += 1
        if g_arr[i][j] != 0:
            counts += 1
    
print(score)
print(counts)
    
