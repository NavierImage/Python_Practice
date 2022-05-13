n = int(input())
m = int(input())
num = list(map(int, input().split()))
num.sort()

x = 0
y = n - 1
dama = 0

while(1):
    if x >= y:
        break
    if num[x] + num[y] < m:
        x += 1
    elif num[x] + num[y] > m:
        y -= 1
    else:
        dama += 1
        x += 1
        y -= 1
        
    
    
print(dama)       
    
        
    
            

