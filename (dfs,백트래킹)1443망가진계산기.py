import sys 
d, p = map(int, sys.stdin.readline().rstrip().split())
sys.setrecursionlimit(10**8)
ans_list =[]
def dfs(num, n, cnt, p, st_num):
    if st_num == 1:
        return 
    
    if cnt == p:
        if len(str(num)) <= n:
            ans_list.append(num)
            
    else:
        for i in range(st_num, 1, -1): #여길 9 로 해버리면 중복되는 경우 발생
            num *= i
            dfs(num, n, cnt+1, p, i)
            num = int(num / i)

if len(str(2 ** p)) > d:
    print(-1)
else:
    dfs(1, d, 0, p, 9)
    print(max(ans_list))

