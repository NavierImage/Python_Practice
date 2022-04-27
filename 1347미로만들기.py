n = int(input())
t = input()
x, y = 0, 0
joy = ['F', 'R', 'L'] #조이스틱은 이 3가지임
dx = [1, -1, 0, 0] #RLTB 
dy = [0, 0, 1, -1] #좌표 이동할 것
rcnt = 100

x_list = [0]
y_list = [0]

for i in t:
    nx = 0
    ny = 0
    fcnt = 0
    if i == 'L':
        rcnt += 1 #L, R 방향 나올때마다 기준 100을 조절
    if i == 'R':
        rcnt -= 1
    #방향은 4개, 100을 4로나누어 나머지가 1인건 오른쪽으로, 나머지가 2인건 위쪽으로
    #나머지가 3인건 왼쪽, 나머지가 0인건 아랫쪽으로 이동을 하게하는거
    if rcnt % 4 == 0: #나머지 0이면 아랫쪽
        if i == 'F':  
            nx = x + dx[3]
            ny = y + dy[3]
            fcnt += 1
    elif rcnt % 4 == 1: #나머지 1이면 오른쪽
        if i == 'F':
            nx = x + dx[0]
            ny = y + dy[0]
            fcnt += 1
    elif rcnt % 4 == 2: #나머지 2이면 위쪽
        if i == 'F':
            nx = x + dx[2]
            ny = y + dy[2]
            fcnt += 1
    elif rcnt % 4 == 3: #나머지 3이면 왼쪽
        if i == 'F':
            nx = x + dx[1]
            ny = y + dy[1]
            fcnt += 1
    if fcnt: #움직였을때만 좌표변화가 있으므로 그때만 각 좌표를 기록해둚
        x, y = nx, ny
        x_list.append(x)
        y_list.append(y)

mat = []
for i in range(max(y_list) - min(y_list) + 1):
    temp = []
    for j in range(max(x_list) - min(x_list) + 1):
        temp.append('#')
    mat.append(temp) #움직인 범위의 정수 좌표를 하나 만들어줌

a = min(x_list) #x좌표 최솟값
b = min(y_list) #y좌표 최솟값
if a < 0:
    for i in range(len(x_list)):
        x_list[i] = x_list[i] + abs(a) #움직인 범위의 정사각형을 원점으로 평행이동 해줌
if b < 0:
    for i in range(len(y_list)):
        y_list[i] = y_list[i] + abs(b)

for i in range(len(x_list)):
    for j in range(i, i + 1):
        mat[y_list[j]][x_list[i]] = '.'
    
#출력
for i in range(len(mat) - 1, -1, -1):
    for j in mat[i]:
        print(j, end = '')
    print()
#https://www.acmicpc.net/problem/1347