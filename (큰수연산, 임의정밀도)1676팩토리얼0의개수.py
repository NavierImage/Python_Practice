def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)

n = int(input())
r = str(fac(n))
cnt = 0
for i in range(len(r)-1, -1, -1):
    if r[i] == '0':
        cnt += 1
    else:
        break
print(cnt)