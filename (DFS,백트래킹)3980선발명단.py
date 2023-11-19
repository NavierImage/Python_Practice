import sys
C = int(sys.stdin.readline().rstrip())

def dfs(num_list): #num_list에 들어간 순서 (i번째 선수), num_list에 들어간 숫자 (i번째 선수의 j 포지션)
    if len(num_list) == 11:
        total_list.append(num_list[:])
        return 
    else:
        for i in range(11):
            if visit[i] == 0:
                if arr[len(num_list)][i] == 0: # i번째 선수 j포지션 능력치가 0이면 넘어가기
                    continue
                visit[i] = 1
                num_list.append(i)
                dfs(num_list)
                num_list.pop()
                visit[i] = 0
                
for testcase in range(C):
    arr = []
    for i in range(11):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    visit = [0] * 11
    total_list = []
    dfs([])
    value = 0
    for idx_list in total_list:
        temp = 0
        for i, j in enumerate(idx_list):
            temp += arr[i][j]
        value = max(value, temp)
    print(value)
