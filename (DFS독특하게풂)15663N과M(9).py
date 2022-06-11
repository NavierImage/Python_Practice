import sys
import copy
n, m = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))
num.sort()
s = []
result = []
counter = {} #원소 갯수 셀 딕셔너리

for value in num: #주어진 원소 갯수 세줌.
    try: counter[value] += 1 #해보고
    except: counter[value] = 1 #안되면 추가해라 라는 문법으로 보임

def dfs(s):
    global result #원래면 global m, global counter 해줘야 
    if len(s) == m:
        p = s[:]
        result.append(p)
            
    else: #하기 방식은 정렬했다는 가정하에 맞는거.
        prei = 0 #nber 하나 이전꺼
        for idx, nber in enumerate(num):
            if idx > 0: #첫번째꺼 지난경우에만
                prei = num[idx-1] #이전꺼 idx이용하여 prei변수에 초기화
            if prei == nber:
                continue #만약 지금 number가 이전꺼랑 같다면 다음 꺼로 넘어감

            if counter[nber] > 0: 
                pass #지금 number 갯수를 다 사용하지 않았다면 pass
            else:continue #0이면 number갯수를 다쓴거니깐 다음꺼
            
            s.append(nber) 
            counter[nber] -= 1 #하나씩 쓰고
            dfs(s)
            counter[nber] += 1 #나올때 다시 하나씩 넣어줌
            s.pop()
            
dfs(s)
for i in result:
    print(*i)
#https://www.acmicpc.net/problem/15663
