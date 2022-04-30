n = input()
num = []
for i in n:
    num.append(int(i))
num.sort()  #버블소트로도 구현가능
res = []
cnt69 = 0
for i in num:
    if i == 6 or i == 9:
        cnt69 += 1

need6and9 = cnt69//2 + cnt69 % 2 #6이랑 9가 필요한건 6과 9의 존재 수를 2로나눈몫과 나머지만큼 필요함
scnt = 1
same = []
flag = 0

for i in range(len(num) - 1):
    if num[i] == 6 or num[i] == 9:
        continue
    if num[i] == num[i + 1]:
        scnt+=1
    else:
        scnt = 1
    same.append(scnt)

same.append(1) #same이 비는경우도 있어서 그냥 초깃값 넣어버림
res = []

res.append(need6and9)
res.append(max(same))
print(max(res)) 
#6과 9의 개수, 그 외숫자들의 개수가 총 얼마나 필요한지 결정짓게만드므로 그중에 가장 요구값이 큰걸 출력
#https://www.acmicpc.net/problem/1475
