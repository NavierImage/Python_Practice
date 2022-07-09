#외적 아이디어를 통해 CCW인지 CW인지 확인가능
import sys 
from collections import deque
coord = []
for _ in range(3):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    coord.append((x, y))

x1, y1 = coord[0]
x2, y2 = coord[1]
x3, y3 = coord[2]

i1, j1 = x2-x1, y2-y1
i2, j2 = x3-x2, y3-y2
cross = i1*j2 - i2*j1
if cross > 0:
    print(1)
elif cross == 0:
    print(0)
else:
    print(-1)
#https://www.acmicpc.net/problem/11758