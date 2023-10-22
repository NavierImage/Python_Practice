import sys 
import re
tc = int(sys.stdin.readline().rstrip())
convert = {"+" : 0, "-" : 1, " " :2 }
num_total = ["+", "-", " "]

def dfs(num_list):
    if len(num_list) == N-1:
        op_list.append(num_list[:])
        return 
    else:
        for i in range(len(num_total)):
            num_list.append(num_total[i])
            dfs(num_list)
            num_list.pop()
final_ans_list = []
for _ in range(tc):
    N = int(sys.stdin.readline().rstrip())
    
    op_list = []
    dfs([])
    ans_list = []
    for op in op_list:
        template = ""
        tmp_num = 0
        for i in range(len(op)):
            
            template += str(i+1)
            template += op[i]
        template += str(len(op)+1)
        if tmp_num == 0:
            ans_list.append(template)
    ans_new_list =[]
    for nom in ans_list:
        tmp = str(nom)
        dd = re.sub(r"\s", "",tmp)
        ans_new_list.append(dd)
    
    real_ans_list = []

    for ind, string in enumerate(ans_new_list):
        nums = re.findall(r'\d+', string)
        ops = re.findall(r"\D+", string)
        if len(ops) == 0:
            ans = int(nums[0])
            continue
        ans = None
        for i in range(len(ops)):
            if i == 0:
                if ops[i] == "+":
                    ans = int(nums[i]) + int(nums[i+1])
                else:
                    ans = int(nums[i]) - int(nums[i+1])
            else:
                if ops[i] == "+":
                    ans += int(nums[i+1])
                else:
                    ans -= int(nums[i+1])
        
        if ans == 0:
            real_ans_list.append(ans_list[ind])
    real_ans_list.sort()
    final_ans_list.append(real_ans_list)

for i in range(len(final_ans_list)):
    for j in range(len(final_ans_list[i])):
        print(final_ans_list[i][j])
    if i < len(final_ans_list)-1:
        print()
    else:
        pass