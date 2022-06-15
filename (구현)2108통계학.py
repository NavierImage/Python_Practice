import sys
n = int(sys.stdin.readline().rstrip())
numlist = []
for i in range(n):
    numlist.append(int(sys.stdin.readline().rstrip()))
numlist.sort()   
num_dict = {} 
mean = sum(numlist)/len(numlist) 
median = numlist[len(numlist)//2]

for i in numlist:
    try: num_dict[i] += 1
    except: num_dict[i] = 1 #해당 값에 대해 count를 가진 dictionary

max_num = max(num_dict.values()) #value중 최댓값 

modelist =[]
for i in num_dict: #dictionary별로 value 비교해가면서 같으면 modelist에 추가
    if num_dict[i] == max_num: 
        modelist.append(i)
if len(modelist) > 1: #여러개 있다면 dict는 이미 정렬된 값이므로 두번째값을 mode로 설정
    mode = modelist[1]
else: #하나만 있다면 그게 mode.
    mode = modelist[0]
#오래 걸릴 것 같았으나, 시간복잡도가 N이라서..
print(round(mean))
print(median)
print(mode)
print(max(numlist)-min(numlist))