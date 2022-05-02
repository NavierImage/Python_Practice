a, b = input().split()
dif = abs(len(a) - len(b)) + 1
rlt = []
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