t = int(input())
b = [1, 0, 0]
for i in range(t):
    x, y = map(int, input().split())
    b[x - 1], b[y - 1] = b[y - 1], b[x - 1] #공의 위치를 옮기는거로 생각해도됨.

print(b.index(1) + 1)
#https://www.acmicpc.net/problem/1547