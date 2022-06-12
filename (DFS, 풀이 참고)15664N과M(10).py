import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))
num.sort()
s = []
result = []
counter = {} 

for value in num: 
    try: counter[value] += 1 
    except: counter[value] = 1 

def dfs(s):
    global result 
    if len(s) == m:
        p = s[:]
        result.append(p)
            
    else: 
        prei = 0 #이 부분이 중요
        for idx, nber in enumerate(num):
            
            if idx > 0: #정렬이되어있어야 이렇게 사용가능, 현재 인덱스의 값, 이전 인덱스 값과 비교
                prei = num[idx-1] 
            if prei == nber: #같다면 중복이므로 거름
                continue 

            if counter[nber] > 0: #자기 자신 중복을 거르기 위해서
                pass 
            else:continue 

            if len(s) > 0:
                if nber < s[len(s) -1]:
                    continue

            s.append(nber) 
            counter[nber] -= 1 
            dfs(s)
            counter[nber] += 1 
            s.pop()
            
dfs(s)
for i in result:
    print(*i)