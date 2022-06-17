import sys
from itertools import combinations
n, m, d = map(int, sys.stdin.readline().rstrip().split())
comb = []
for i in range(m):
    comb.append((n, i))

board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
cb = []
res = []
for i in board:
    cb.append(i[:])

for arpo in combinations(comb, 3): #이것 조합 구하는 부분 DFS로 구현해볼 수도 있으나 그냥... 파이썬을 이용
    cnt =0
    kill = 0
    while board:  
        #한턴 시작
        ardict = [{}, {}, {}]#key: 거리 value: 좌표
        #궁수별로 각 적에 대한 거리와 좌표정보를 담은 딕셔너리를 담은 리스트 

        for i in range(len(board)-1, -1, -1): #비효율적이나,, 그냥 했음(행에 대해서는 d만큼만 반복해도되나 구현이 귀찮아 그냥햇음)
            for j in range(len(board[i])):
                if board[i][j] == 1: #적이 있다면
                    for idx, archer in enumerate(arpo): #세 궁수에 대해 거리를 각각 구해서 , 거리를 key, 좌표를 value로 dictionary에 넣어줌
                        y, x = archer
                        y += cnt #궁수의 행 좌표도 같이 줄어드니깐 y값을 음수 cnt더해서 업뎃
                        dist = abs(y-i)+abs(x-j)
                        try:ardict[idx][dist].append((i, j))
                        except:ardict[idx][dist] = [(i, j)]
        
        killed = [] #동시에 쏴죽이는것을 판단하기 위한 killed list
        for dicts in ardict: 
            if len(dicts) != 0:
                if min(dicts.keys()) <= d: #궁수1, 궁수2, 궁수3 돌아가면서, key가 거리이므로 거리의 최솟값 구함
                    dicts[min(dicts.keys())].sort(key=lambda x:x[1]) #value는 좌표이므로, 같은 거리인 좌표가 여러개있으면 왼쪽부터 제거할것이므로 좌표를 
                    #열 기준으로 정렬
                    dr, dc = dicts[min(dicts.keys())][0] #정렬하고 나면 해당 딕셔너리의 value 배열에서 가장 왼쪽에 있는것이 같은 최솟값을 가진 여러개 좌표들중 가장 왼쪽인것임.
                    if (dr, dc) not in killed:#이미 다른 궁수가 잡았다면 kill을 올릴필요가 없음.(동시에 쏴죽이는것)
                        kill += 1 
                        killed.append((dr, dc))
                    board[dr][dc] = 0
        board.pop() #가장 밑행 pop(한턴 끝)
        cnt -= 1 #cnt1 깎아줌(줄어드는 궁수의 행좌표를 구현하기 위한것)

    for i in cb:
        board.append(i[:])
    res.append(kill)
print(max(res))
#https://www.acmicpc.net/problem/17135
