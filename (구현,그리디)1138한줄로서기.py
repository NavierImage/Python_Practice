
import sys 
n = int(sys.stdin.readline().rstrip())
infoarr = list(sys.stdin.readline().rstrip().split())
for i in range(len(infoarr)):
    infoarr[i] = int(infoarr[i])
infoarr_rev = infoarr[::-1]
arr = [i + 1 for i in range(len(infoarr))]
arr_rev = arr[::-1]

rst_list = [arr_rev[0]]

    
idx = 1 
while len(rst_list) < n:
    num = arr_rev[idx]
    info = infoarr_rev[idx]

    cnt = 0
    if cnt == info:
        rst_list.insert(cnt, num)
        idx += 1 
        continue

    for val in rst_list:
        if val > num:
            cnt += 1 
        if cnt == info:
            rst_list.insert(cnt, num)
            break
        
        
    idx += 1
print(*rst_list)

