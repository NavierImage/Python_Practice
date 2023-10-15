import sys 
N = int(sys.stdin.readline().rstrip())

length_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 9876543210 이것보다 더 감소할 수는 없음
num_total_list = [i for i in range(9, -1, -1)] # 숫자의 재료. 9~0 으로 되게.

def dfs(num_list, L): #백트래킹 구현. 
    if len(num_list) == L:
        temp_ans_list.append(num_list[:])
    else:
        for i in range(len(num_total_list)):
            if visited[i] == 1:
                continue
            if len(num_list) > 0: #조합 구현. num_list에있는 마지막 숫자가 더 작으면 안부르게.
                if num_list[-1] < num_total_list[i]:
                    continue
            visited[i] = 1
            num_list.append(num_total_list[i])
            dfs(num_list, L)
            num_list.pop()
            visited[i] = 0
ans_tot_list = []
for L in length_list: # length 순서대로 조합으로 구해주기.
    visited = [0] * 10
    temp_ans_list = []
    dfs([], L)
    temp_ans_list.reverse()
    for i in range(len(temp_ans_list)):
        temp_str = ""
        for j in range(len(temp_ans_list[i])):
            temp_str += str(temp_ans_list[i][j])
        ans_tot_list.append(temp_str)
try:
    print(ans_tot_list[N])
except:
    print(-1)