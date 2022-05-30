import sys
#시간복잡도에대해 잘 고려해봐야하는 문제...
q = list(sys.stdin.readline().rstrip().upper())
sq = list(set(q))
res = []
stt = []
flag = 0
for i in range(len(sq)): #순회를 한번만 해야 ㅜ
    d = q.count(sq[i])
    res.append(d)
    stt.append(sq[i])
cnt = 0
for i in res:
    if max(res) == i:
        cnt+=1
    if cnt>=2:
        print('?')
        break
else:print(stt[res.index(max(res))])

