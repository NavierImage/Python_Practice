import sys 
n = int(sys.stdin.readline().rstrip())
cmd_list = []
for i in range(n):
    cmd_list.append(list(sys.stdin.readline().rstrip().split()))

# 뒤집어서 undo걸리는 곳만 다 없애고 type하는거만 골라내면 정답이됨!

cmd_list.reverse()


no_append = int(cmd_list[0][2])+1

real_cmd_list = []
for i, cmd in enumerate(cmd_list):
    time_now = int(cmd[2])

    
    if no_append <= time_now:
        continue
    elif no_append > time_now:
        pass

    if cmd[0] == "undo":
        no_append = int(cmd[2]) - int(cmd[1])
        real_cmd_list.append(cmd)
    else:
        real_cmd_list.append(cmd)
real_cmd_list.reverse()


type_str = ""
done_chk = 0
for cmd in real_cmd_list:
    if cmd[0] == "type":
        type_str = type_str + cmd[1]
        done_chk = 1

print(type_str)


