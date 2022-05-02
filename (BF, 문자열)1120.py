a, b = input().split()
dif = abs(len(a) - len(b)) + 1
rlt = []
#어차피 붙일거는 긴거랑 똑같으니깐, 겹치는 문자가 제일 많은걸 잡아두면됨(안겹치는게 제일 적을때)
#뭘 얼마나 붙일지는 생각안해도되고, 그냥 겹치는게 제일 많을때 문제에서 정의하는 차이수도 제일 적으니
#전부 대조하여 그때를 구하면됨. 함수화 시켜서 구할수도있으나 그냥 귀찮아서 다 
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
#https://www.acmicpc.net/problem/1120
