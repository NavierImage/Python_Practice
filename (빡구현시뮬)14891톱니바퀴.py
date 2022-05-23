def gearrotate(g, rot): #rot 방향에 따라 gear를 회전시켜주는 함수
    if rot == 1:    
        g = g[7] + g[0:7]
    elif rot == -1:
        g = g[1:]+ g[0]
    result = g
    return result 

gear = []
for i in range(4):
    g = input()
    gear.append(g)
k = int(input())
#N극은 0 S극은 1

gearnum = []
dir = [] #돌릴 기어와 방향 정하기
for i in range(k):
    w, d = map(int, input().split())
    w -= 1
    gearnum.append(w)
    dir.append(d) 

for i in range(k):
    check = [0, 0, 0, 0] #기어가 돌아갈지 안돌아갈지 결정하는 list
    dirset = [0, 0, 0, 0]
    link = 0 #link여부 확인하는 식으로
    if gearnum[i] == 0:
        check[0] = 1
        if gear[0][2] != gear[1][6]:
            link = 1
            check[1] = 1
        if gear[1][2] !=  gear[2][6] and link == 1: 
            check[2] = 1
        else:
            link = 0
        if gear[2][2] != gear[3][6] and link == 1:
            check[3] = 1

    elif gearnum[i] == 1:
        check[1] = 1
        if gear[1][6] != gear[0][2]: #왼
            check[0] = 1
        if gear[1][2] != gear[2][6]: 
            link = 1
            check[2] = 1
        if gear[2][2] != gear[3][6] and link == 1:
            check[3] = 1
    
    elif gearnum[i] == 2:
        check[2] = 1
        if gear[2][2] != gear[3][6]:
            check[3] = 1
        if gear[2][6] != gear[1][2]:
            check[1] = 1
            link = 1
        if gear[1][6] != gear[0][2] and link == 1:
            check[0] = 1
    
    elif gearnum[i] == 3:
        check[3] = 1
        if gear[3][6] != gear[2][2]:
            check[2] = 1
            link = 1
        if gear[2][6] != gear[1][2] and link == 1:
            check[1] = 1
        else:
            link = 0
        if gear[1][6] != gear[0][2] and link == 1:
            check[0] = 1
    #케이스마다 연결 여부 확인
    
    if gearnum[i] % 2 == 0: #짝수인덱스 기어마다 같은 방향, 홀수인덱스 기어마다 같은 방향
        dirset[0], dirset[2] = dir[i], dir[i]
        dirset[1], dirset[3] = dir[i]*(-1), dir[i]*(-1)
    else:
        dirset[1], dirset[3] = dir[i], dir[i]
        dirset[0], dirset[2] = dir[i]*(-1), dir[i]*(-1)
    ngear = gear[:]
    #위 정보 맞춰서 회전시켜줌(check 1일시 회전)
    for j in range(4):
        if check[j] == 1:
            ngear[j] = gearrotate(gear[j], dirset[j])
    
    gear = ngear[:]

cnt = 0
score = 0
for g in gear:
    if g[0] == '1':
        score += 2**cnt
    cnt += 1
print(score)