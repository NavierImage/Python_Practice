import sys
n = int(sys.stdin.readline().rstrip())
find = int(sys.stdin.readline().rstrip())
board = [[0] * n for _ in range(n)]
idx_dict = {}
idx = 0
#정사각형일때고 사실 직사각형가면 개피곤해쥠..
for i in range(n//2+1):
    for j in range(i, n-i-1):
        board[j][i] = n**2 - idx
        idx_dict[n**2-idx] = (j, i)
        idx += 1
    for j in range(i, n-i-1):
        board[n-i-1][j] = n**2 - idx
        idx_dict[n**2-idx] = (n-i-1, j)
        idx += 1
    for j in range(n-i-1, i, -1):
        board[j][n-i-1] = n**2 - idx
        idx_dict[n**2-idx] = (j, n-i-1)
        idx += 1
    for j in range(n-i-1, i, -1):
        board[i][j] = n**2 - idx
        idx_dict[n**2-idx] = (i, j)
        idx += 1
if board[n//2][n//2] == 0:
    board[n//2][n//2] = 1
    idx_dict[1] = (n//2, n//2)
#오답코드
#idx_dict[1] = (n//2, n//2)
#board[n//2][n//2] = 1
for i in board:
    print(*i)
a, b = idx_dict[find]
print(a+1, b+1)

#오답코드이나 정답처리됨.ㅋㅋ