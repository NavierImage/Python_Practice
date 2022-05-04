import re
n = input()
numst = n.split('-')
num = []
for i in numst:
    ptsum = 0
    enco = re.findall('\d+', i)
    for j in enco:
        ptsum += int(j)
    num.append(ptsum)

res = num[0]
if len(num) > 1:
    for i in range(1, len(num)):
        res -= num[i]
else:
    pass

print(res)