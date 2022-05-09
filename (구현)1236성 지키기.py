n, m = map(int, input().split())
cat = []
for i in range(n):
    s = input()
    cat.append(s)

rcnt = 0
for i in range(n): #행 돌면서 열마다 검사
    for j in range(len(cat[i])): 
       if cat[i][j] == 'X':
           break
    else:
        rcnt += 1

ccnt = 0
for j in range(m): #열 돌면서 행마다 검사
    for i in range(n):
        if cat[i][j] == 'X':
            break
    else:
        ccnt += 1
#그중에 제일 많이 채워야하는거 채우면됨.. 어차피 정확히 어디 채울거냐 따지는게아니니
#열과 행이 동시에 비는경우 동시에 채우는 지점이 항상 존재하니까
print(max(rcnt, ccnt))
