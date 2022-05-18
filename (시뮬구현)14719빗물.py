h, w = map(int, input().split())
bck = list(map(int, input().split()))
world = []
for i in range(h):
    temp =[]
    for j in range(w):
        temp.append(0)
    world.append(temp) #세계를 0으로 만들고

for j in range(w):
    for i in range(bck[j]):
        world[h-1-i][j] = 1 #행렬 전치 시켜서 밑에서부터 블록수대로 쌓아주고

lswitch = 0 
s = 0
for i in range(h):
    lswitch = 0
    for j in range(w-1):
        if world[i][j] == 1 and world[i][j+1] == 0:
            lswitch = 1 #1-0으로 들어오면 왼쪽스위치 켜짐
            left = j #해당 블록의 인덱스 저장
        elif world[i][j] == 0 and world[i][j+1] == 1 and lswitch == 1: #왼쪽스위치가 켜져있고 0-1일때
            right = j
            bincan = right - left #앞에서 저장한 인덱스와 현재 블록의 인덱스를 뺀게 빈칸임
            lswitch = 0
            s += bincan #빈칸을 계속 추가

print(s)
#https://www.acmicpc.net/problem/14719
#더좋은아이디어가있었을듯 최대 값기준으로 하는...