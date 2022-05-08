s = list(input())
cnt = 0

for i in range(len(s) - 3):
    if s[i] == 'X' and s[i+1] == 'X' and s[i+2] == 'X' and s[i+3] == 'X':
        s[i] = 'A'
        s[i + 1] ='A'
        s[i + 2] = 'A'
        s[i + 3] = 'A'

for i in range(len(s) - 1):
    if s[i] == 'X' and s[i + 1] == 'X':
        s[i] = 'B'
        s[i + 1] = 'B'

sr = "".join(s)

if 'X' in sr:
    print(-1)
else:
    print(sr)
