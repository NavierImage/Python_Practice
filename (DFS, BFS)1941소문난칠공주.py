import sys
from collections import deque 
arr = []
for i in range(5):
    arr.append(list(sys.stdin.readline().rstrip()))

idx_dict = {}

idx = 0
for i in range(5):
    for j in range(5):
        idx_dict[idx] = (i, j)
        idx += 1

total_num_list = [i for i in range(25)]

#위치를 1차원으로 바꿔서 조합을 구하기
ans_list = []
def dfs(num_list):
    global ans_list
    if len(num_list) == 7:
        
        ans_list.append(num_list[:])
        return 
    else:
        for i in range(len(total_num_list)):
            if len(num_list) > 0:
                if num_list[-1] >= total_num_list[i]:
                    continue
            num_list.append(total_num_list[i])
            dfs(num_list)
            num_list.pop()

#연결요소 체크용

def bfs(y, x):
    queue = deque()
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    visited = [[0] * 5 for _ in range(5)]
    visited[y][x] = 1
    queue.append((y, x))
    while queue:
        y, x=  queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<5 and 0<=nx<5:
                if check_arr[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))
    return visited

dfs([])

ans_cnt = 0
for ans in ans_list:
    check_arr = [[0] * 5 for _ in range(5)]
    s_cnt = 0
    for idx in ans:
        i, j = idx_dict[idx]
        check_arr[i][j] = 1
        if arr[i][j] == 'S':
            s_cnt += 1
    if s_cnt < 4:
        continue
    visit = bfs(i, j)
    if visit == check_arr:
        ans_cnt+=1

    # for a in check_arr:
    #     print(a)
    # print()
    # for v in visit:
    #     print(v)
    # quit()
print(ans_cnt)

