import sys
N = int(sys.stdin.readline().rstrip())
nb = list(map(int, sys.stdin.readline().rstrip().split()))
nb.sort()
M = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
result =[]
########이분탐색###########
#first와, last index, 그리고 그중간의 middle index잡음
#1.만약 찾을 값이 middle index보다 크다면 -> middle index가 first index가 되고, middle index 업데이트
#2.만약 찾을 값이 middle index보다 작다면 -> middle index가 last index가되고, middel index 업데이트
#ㅜㅜ헷갈리다니..
for i in nums:
    j = 0
    fir = 0
    last = len(nb) -1
    mid = (fir+last)//2 
    while(1):
        flag = 0
        if i == nb[fir] or i == nb[last]:
            result.append(1)
            break
        if i < nb[mid]:
            last = mid
            mid = (fir+last)//2
        elif i > nb[mid]:
            fir = mid
            mid = (fir+last)//2
        elif i == nb[mid]:
            result.append(1)
            flag = 1
            break

        if fir == mid and flag == 0:
            result.append(0)
            break
for i in result:
    print(i)