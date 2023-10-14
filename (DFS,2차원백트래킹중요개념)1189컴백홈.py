import sys 
sys.setrecursionlimit(10**9)
r, c, k = map(int, sys.stdin.readline().rstrip().split())

arr = []
for i in range(r):
    arr.append(list(sys.stdin.readline().rstrip()))

visited = [[0] * c for _ in range(r)]
recur_list = []
def dfs(y, x, recur_cnt):
    
    if y == 0 and x == c-1:
        
        recur_list.append(recur_cnt)
        return
    else:
        if y < 0 or y >= r or x < 0 or x >= c:
            return
        if arr[y][x] == "T":
            return 
        if visited[y][x] == 1:
            return
        visited[y][x] = 1
        #for 문으로 줄일 수 있음.
        dfs(y+1, x, recur_cnt+1)
        dfs(y-1, x, recur_cnt+1)
        dfs(y, x+1, recur_cnt+1)
        dfs(y, x-1, recur_cnt+1)
        # 순열,조합 백트래킹의 개념 = 함수끝나고 나올때 visit 풀어줘야 꺾고 들어감.
        visited[y][x] = 0

dfs(r-1, 0, 1)

ans = 0
for val in recur_list:
    if k == val:
        ans += 1
print(ans)
