import sys
import math

n = int(sys.stdin.readline().rstrip())
dragon_curve = []
for _ in range(n):
    x, y, d, g = map(int, sys.stdin.readline().rstrip().split())
    dragon_curve.append((x, y, d, g))

arr = [[0] * 101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for curve in dragon_curve:
    x, y, d, g = curve
    g += 1
    curve_c = []
    for i in range(g):
        if i == 0:
            #모든 케이스에 대하여 중심이 (0, 0)이라고 생각함
            curve_c.append((0, 0))
            curve_c.append((dy[d], dx[d]))

        else:
            st_y, st_x = curve_c[-1]
            for j in range(len(curve_c)-2, -1, -1):
                y1, x1 = curve_c[j]
                movedY, movedX = y1-st_y, x1-st_x #평행이동 (커브의 끝점을 (0, 0)으로)
                new_x, new_y = -movedY, movedX #90도 회전 변환 -> (x, y) 넣은게 (-y, x)로.
                new_y += st_y
                new_x += st_x
                curve_c.append((new_y, new_x))
    for i in range(len(curve_c)):
        b, a = curve_c[i]
        arr[b+y][a+x] = 1
cnt = 0
for i in range(len(arr)-1):
    for j in range(len(arr[i])-1):
        no = 0
        for u in range(2):
            if no:
                break
            for v in range(2):
                if arr[i+u][j+v] == 0:
                    no = 1
                    break
        if no == 1:
            pass
        else:
            cnt += 1
print(cnt)
          