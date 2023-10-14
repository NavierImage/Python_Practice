import sys 
L, C = map(int, sys.stdin.readline().rstrip().split())
str_list = list(sys.stdin.readline().rstrip().split(" "))
str_list.sort() # 문자 정렬
num_convert = {} 
num_total_list = []
for i in range(len(str_list)): # 숫자로 변환
    num_convert[str_list[i]] = i
    num_total_list.append(i)

visited = [0] * len(str_list)

ans_num_list = []
def dfs(num_list): # 숫자 기반 백트래킹

    if len(num_list) == L:
        ans_num_list.append(num_list[:])
        
    else:
        for i in range(len(num_total_list)):
            if visited[i] == 1:
                continue
            if len(num_list) > 0:
                if num_list[-1] > num_total_list[i]:
                    continue
            visited[i] = 1 #visit 걸고
            num_list.append(num_total_list[i]) #추가하고
            dfs(num_list) #재귀
            num_list.pop() # 종료조건으로 함수 끝나면 Pop하고
            visited[i] = 0 # visit 풀고
            # for 문 돌아가서 다음 인덱스로 넘어감
dfs([])
str_convert = {v:k for k, v in num_convert.items()} 

ans_list = []
for i in range(len(ans_num_list)): # 문자로 다시 변환
    temp = []
    for j in range(len(ans_num_list[i])):
        temp.append(str_convert[ans_num_list[i][j]])
    ans_list.append(temp)

vowel_list = ["a", "e", "i", "o", "u"]
for ans in ans_list: #모음 및 자음 조건 거르기
    v_cnt = 0
    for vowel in vowel_list:
        if vowel in ans:
            v_cnt += 1
    c_cnt = len(ans) - v_cnt
    if c_cnt < 2 or v_cnt < 1:
        continue
    a = ''
    for let in ans:
        a += let
    print(a)
