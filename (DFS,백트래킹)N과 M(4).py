import sys 
n, m = map(int, sys.stdin.readline().split())
num = []
visited = [0]*n

def dfs(num):
    if len(num) == m:
        print(*num)
        return
    else:
        for i in range(n):
            flag = 0
            for j in num: #num의 원소들에대해서 
                if len(num) >= 1: #num개수 1보다 많을때
                    if (i+1) < j: #만약 num에 넣을 값이 num의 원소보다 작다면
                        flag= 1 #flag = 1해주고
                        break
            if flag: #flag =1일시 건너뛰게
                continue
                    
            num.append(i+1)
            
            dfs(num)
            num.pop()
            
dfs(num)