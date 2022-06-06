import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())

vill = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    vill.append(temp)

comb = []; house = []
for i in range(n):
    for j in range(n):
        if vill[i][j] == 2:
            comb.append((i, j))
        if vill[i][j] == 1:
            house.append((i, j))
minimum = []
for h in combinations(comb, m): #치킨집의 좌표, 집의 좌표 해서 조합으로풀면 됨
    totdist = 0
    for i in house:
        r1, c1 = i
        distmin =110 #문제 조건에 영향 안받을 최대거리로 두고
        for j in h:
            r2, c2 = j
            dist = abs(r1-r2)+abs(c1-c2)
            if distmin > dist: #더 작은 dist값을 발견하면 distmin을 업데이트
                distmin = dist
        totdist += distmin   

        
    minimum.append(totdist)

print(min(minimum))