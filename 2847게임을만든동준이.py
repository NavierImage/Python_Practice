##2847##
import sys
n = int(sys.stdin.readline().rstrip())
level = []
for _ in range(n):
    level.append(int(sys.stdin.readline().rstrip()))

cnt = 0
for i in range(n-2, -1, -1):
    if level[i+1] > level[i]:
        pass
    else:
        cnt += level[i]+1-level[i+1]
        level[i] -= (level[i]+1-level[i+1])
        
print(cnt)