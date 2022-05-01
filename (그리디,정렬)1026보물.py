n = int(input())
num =[]
for i in range(2):
    t = input()
    num.append(t.split(' '))

for i in range(2):
    for j in range(len(num[i])):
        num[i][j] = int(num[i][j])

num[0].sort()
num[1].sort()
num[1].reverse()
res= []
for i in range(n):
    res.append(num[0][i] * num[1][i])

print(sum(res))
#걍 하나는 오름차순 하나는 내림차순으로 해서 곱하면 되는거아닌가?
#왜 배열을 바꾸지 말라는 조건이있는지는 모르겟다 최솟값과 연관이없음
#문자열 띄어써서 입출력 받을때 list(map(int, input().split()))으로 할수 있다!
#정렬없이 각각 최솟값 최댓값 구하여 곱하고 지워도됨
#https://www.acmicpc.net/problem/1026