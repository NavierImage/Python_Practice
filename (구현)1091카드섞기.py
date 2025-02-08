import sys 

n = int(sys.stdin.readline().rstrip())
p = list(map(int, sys.stdin.readline().rstrip().split()))
s = list(map(int, sys.stdin.readline().rstrip().split()))

card_list = []

for card_num in range(len(s)):
    card_list.append(chr(65+card_num))

objective_dict = {}
for idx, player in enumerate(p):
    if player in objective_dict:
        objective_dict[player].append(card_list[idx])
    else:
        objective_dict[player] = [card_list[idx]] #처음 기준으로...


# 0 check 
rst_dict = {}
p_start = [0, 1, 2] * (n//3)
for idx, player in enumerate(p_start):
    if player in rst_dict:
        rst_dict[player].append(card_list[idx])
    else:
        rst_dict[player] = [card_list[idx]] #처음 기준으로...
cnt = 0
flag = 0
for key, val in rst_dict.items():
    val.sort() 
    if objective_dict[key] == val:
        pass 
    else:
        flag = 1
        break
if flag:
    pass 
else:
    print(cnt)
    quit()

start_card_list = card_list[:]

while True:
    new_card_list = card_list[:]
   
    for i, co in enumerate(s):
        new_card_list[co] = card_list[i]
    

    card_list = new_card_list[:]
    rst_dict = {}
    for idx in range(len(p_start)):
        if p_start[idx] in rst_dict:
            rst_dict[p_start[idx]].append(new_card_list[idx])
        else:
            rst_dict[p_start[idx]] = [new_card_list[idx]]
    flag = 0
    for key, val in rst_dict.items():
        val.sort() 
        if objective_dict[key] == val:
            pass 
        else:
            flag = 1
            break
    if flag:
        pass 
    else:
        break

    # print(new_card_list)
    cnt += 1
    if new_card_list == start_card_list:
        print(-1)
        quit()
print(cnt+1)