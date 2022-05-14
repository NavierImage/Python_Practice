#https://www.acmicpc.net/problem/14500
n, m = map(int, input().split())
mat = []
for i in range(n):
    r = list(map(int, input().split()))
    mat.append(r)

rlt = []
for i in range(n): #가로 일직선
    for j in range(m - 3):
        s1 = 0
        for v in range(j, j + 4):
            s1 += mat[i][v]
        rlt.append(s1)

print(rlt)

for j in range(m): #세로 일직선
    for i in range(n - 3):
        s2 = 0
        for u in range(i, i+4):
            s2 += mat[u][j]
        rlt.append(s2)
print(rlt)
#2by2를안햇넹
for i in range(n - 1):
    for j in range(m - 1):
        temp = []
        for u in range(i, i + 2):
            for v in range(j, j + 2):
                temp.append(mat[u][v])
        rlt.append(sum(temp))
sixh = []
#2by3-1
for i in range(n - 1):
    for j in range(m - 2):
        temp = []
        for u in range(i, i+2):
            for v in range(j, j+3):
                temp.append(mat[u][v])
        temp[0] = 0
        temp[1] = 0
        rlt.append(sum(temp))

for i in range(n - 1):
    for j in range(m - 2):
        temp = []
        for u in range(i, i+2):
            for v in range(j, j+3):
                temp.append(mat[u][v])
        temp[1] = 0
        temp[2] = 0
        rlt.append(sum(temp))
for i in range(n - 1):
    for j in range(m - 2):
        temp = []
        for u in range(i, i+2):
            for v in range(j, j+3):
                temp.append(mat[u][v])
        temp[3] = 0
        temp[4] = 0
        rlt.append(sum(temp))
for i in range(n - 1):
    for j in range(m - 2):
        temp = []
        for u in range(i, i+2):
            for v in range(j, j+3):
                temp.append(mat[u][v])
        temp[4] = 0
        temp[5] = 0
        rlt.append(sum(temp))
for i in range(n - 1):
    for j in range(m - 2):
        temp = []
        for u in range(i, i+2):
            for v in range(j, j+3):
                temp.append(mat[u][v])
        temp[0] = 0
        temp[2] = 0
        rlt.append(sum(temp))
for i in range(n - 1):
    for j in range(m - 2):
        temp = []
        for u in range(i, i+2):
            for v in range(j, j+3):
                temp.append(mat[u][v])
        temp[3] = 0
        temp[5] = 0
        rlt.append(sum(temp))
for i in range(n - 1):
    for j in range(m - 2):
        temp = []
        for u in range(i, i+2):
            for v in range(j, j+3):
                temp.append(mat[u][v])
        temp[0] = 0
        temp[5] = 0
        rlt.append(sum(temp))
for i in range(n - 1):
    for j in range(m - 2):
        temp = []
        for u in range(i, i+2):
            for v in range(j, j+3):
                temp.append(mat[u][v])
        temp[2] = 0
        temp[3] = 0
        rlt.append(sum(temp))

#3by2
sixv = []
for i in range(n - 2):
    for j in range(m - 1):
        temp = []
        for u in range(i, i+3):
            for v in range(j, j+2):
                temp.append(mat[u][v])
        temp[0] = 0
        temp[2] = 0
        rlt.append(sum(temp))

for i in range(n - 2):
    for j in range(m - 1):
        temp = []
        for u in range(i, i+3):
            for v in range(j, j+2):
                temp.append(mat[u][v])
        temp[2] = 0
        temp[4] = 0
        rlt.append(sum(temp))

for i in range(n - 2):
    for j in range(m - 1):
        temp = []
        for u in range(i, i+3):
            for v in range(j, j+2):
                temp.append(mat[u][v])
        temp[1] = 0
        temp[3] = 0
        rlt.append(sum(temp))

for i in range(n - 2):
    for j in range(m - 1):
        temp = []
        for u in range(i, i+3):
            for v in range(j, j+2):
                temp.append(mat[u][v])
        temp[3] = 0
        temp[5] = 0
        rlt.append(sum(temp))

for i in range(n - 2):
    for j in range(m - 1):
        temp = []
        for u in range(i, i+3):
            for v in range(j, j+2):
                temp.append(mat[u][v])
        temp[0] = 0
        temp[5] = 0
        rlt.append(sum(temp))

for i in range(n - 2):
    for j in range(m - 1):
        temp = []
        for u in range(i, i+3):
            for v in range(j, j+2):
                temp.append(mat[u][v])
        temp[1] = 0
        temp[4] = 0
        rlt.append(sum(temp))

for i in range(n - 2):
    for j in range(m - 1):
        temp = []
        for u in range(i, i+3):
            for v in range(j, j+2):
                temp.append(mat[u][v])
        temp[1] = 0
        temp[5] = 0
        rlt.append(sum(temp))

for i in range(n - 2):
    for j in range(m - 1):
        temp = []
        for u in range(i, i+3):
            for v in range(j, j+2):
                temp.append(mat[u][v])
        temp[0] = 0
        temp[4] = 0
        rlt.append(sum(temp))

print(max(rlt))


