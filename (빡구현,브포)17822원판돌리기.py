import sys
n, m, T = map(int, sys.stdin.readline().rstrip().split())
plate = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    plate.append(temp)

for _ in range(T):
    comd = list(map(int, sys.stdin.readline().rstrip().split()))

    #큐로 구현하는게 빨랐을듯 하나, 문제 사이즈가 시간복잡도에 걸리지 않을 느낌이라 그냥 리스트로 진행
    if comd[1] == 0: #시계 방향의 회전
        for __ in range(comd[2]):
            for i in range(len(plate)):
                if (i + 1) % comd[0] == 0: #리스트는 appendleft가 없어서 insert이용
                    plate[i].insert(0, plate[i].pop(len(plate[i])-1)) 
                    
    elif comd[1] == 1: #반시계 방향의 회전
        for __ in range(comd[2]):
            for i in range(len(plate)):
                if (i + 1) % comd[0] == 0:
                    plate[i].append(plate[i].pop(0))
    #dfs는 마지막-첫번째 껏은 못지워줌.
    plate_copy = []
    for i in plate:
        plate_copy.append(i[:])
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    flag = 0

    #브루트포스 탐색, bfs나 dfs에서 썼지만 하나씩 순회하면서 인접한 4곳을 돌아주는 dx, dy스킬 사용할 수 있음
    for i in range(len(plate)):
        for j in range(len(plate[i])):
            r, c = i, j; nr = 0; nc = 0
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if nr < 0: #행은 순회 구조가 아니므로 범위 밖일시 무시
                    continue
                if nr >= len(plate):
                    continue
                
                if nc < 0: #nc가 0보다 작으면 원판 끝 인덱스로 재선언 
                    nc = len(plate[i])-1

                if nc >= len(plate[i]): #열은 순회 구조이므로 nc가 원판 하나에 적힌 수보다 크면 0으로 재선언
                    nc = 0 

                if plate[r][c] == plate_copy[nr][nc] and plate[r][c] != 0: #plate의 복사본인 plate_copy도 0으로 업뎃되므로, 같은데 0이면 무시해야.
                    plate[r][c] = 0
                    flag = 1 #같은게 있다면 flag 1로

    #flag가 0이라는건 같은게 없다는 말임. 문제 조건에 맞추어 값들 변경해주기.(평균보다 크면 -1, 작으면 +1)
    if flag == 0:
        result = 0
        cnt = 0
        meanval = 0
        for i in plate:
            result += sum(i)
            for j in i:
                if j != 0:
                    cnt += 1
        if cnt != 0:
            meanval = result/cnt

        for i in range(len(plate)):
            for j in range(len(plate[i])):
                if plate[i][j] != 0:
                    if plate[i][j] > meanval:
                        plate[i][j] -= 1
                    elif plate[i][j] < meanval:
                        plate[i][j] += 1

##결과출력##                
rst = 0 
for i in plate:
    rst = rst + sum(i)
print(rst) 