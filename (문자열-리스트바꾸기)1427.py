n = input()
num = []
for i in n:
    num.append(i)
num.sort()
num.reverse()
result = ''
for i in num: #리스트를 다시 문자로 변환하기
    result += i
print(int(result))
#https://www.acmicpc.net/problem/1427