n, x, y = map(int, input().split())
cnt = 0
while(1):
    cnt +=1
    n = (n + 1) // 2
    if x % 2 == 0:
        x = x // 2
    else:
        x = (x + 1) // 2

    if y % 2 == 0:
        y = y // 2
    else:
        y = (y + 1) // 2   
    
    
    if x == y or n == 1:
        break

print(cnt)