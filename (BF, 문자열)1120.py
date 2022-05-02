a, b = input().split()
dif = abs(len(a) - len(b)) + 1
rlt = []
#어차피 붙일거는 긴거랑 똑같으니깐, 겹치는 문자가 제일 많은걸 잡아두면됨(안겹치는게 제일 적을때)
if len(a) > len(b):
    for i in range(dif):
        dcnt = 0
        for j in range(i, i + len(b)):
            if a[j] != b[j]:
                dcnt += 1  
            else:
                pass
        rlt.append(dcnt)
else:
    for i in range(dif):
        dcnt = 0
        for j in range(i, i + len(a)):
            if a[j - i] != b[j]:
                dcnt += 1
            else:
                pass
        rlt.append(dcnt)


print(min(rlt))
