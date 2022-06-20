import sys
board = []
for _ in range(5):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
result = []
tmp = []
def dfs(r, c, tmp):
    if len(tmp) == 6:
        tmpc = tmp[:]
        if tmpc not in result:
            result.append(tmpc)
        return
    if r < 0 or c < 0 or r >= 5 or c >= 5:
        return
    else:
        tmp.append(board[r][c])
        dfs(r-1, c, tmp)
        dfs(r+1, c, tmp)
        dfs(r, c+1, tmp)
        dfs(r, c-1, tmp)
        #선택지가 없을 때 최종적으로 나오면서 pop을 해주는것임.
        tmp.pop()

for i in range(5):
    for j in range(5):
        dfs(i, j, tmp)
print(len(result))
#https://www.acmicpc.net/problem/2210