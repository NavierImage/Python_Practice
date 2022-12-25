import sys
import copy
tc = int(sys.stdin.readline().rstrip())

ans_list = []
for _ in range(tc):
    up = [['w'] * 3 for _ in range(3)]
    down = [['y'] * 3 for _ in range(3)]
    front = [['r'] * 3 for _ in range(3)]
    back = [['o'] * 3 for _ in range(3)]
    left = [['g'] * 3 for _ in range(3)]
    right = [['b'] * 3 for _ in range(3)]
    cmd_n = int(sys.stdin.readline().rstrip())
    cmd_list = list(sys.stdin.readline().rstrip().split(' '))
    #print(cmd_list)
    for i, cmd in enumerate(cmd_list):
        if cmd == 'U+':
            new_pl = [[0] * 3 for _ in range(3)]
            for j in range(2, -1, -1):
                for i in range(3):
                    new_pl[i][j] = up[2-j][i]
            up = copy.deepcopy(new_pl)

            rot_list = [back, right, front, left]
            temp = []
            
            ij_list = [[(0, 2), (0, 1), (0, 0)], [(0, 2), (0, 1), (0, 0)],
            [(0, 2), (0, 1), (0, 0)],[(0, 2), (0, 1), (0, 0)]]
        
            for i in range(len(rot_list)):
                tmp = []
                for j in range(3):
                    y, x = ij_list[i][j]
                    tmp.append(rot_list[i][y][x])
                temp.append(tmp)
            temp.insert(0, temp.pop(-1))
            
            for i in range(len(rot_list)):
                for j in range(3):
                    y, x = ij_list[i][j]
                    rot_list[i][y][x] = temp[i][j]

        elif cmd == 'U-':
            new_pl = [[0] * 3 for _ in range(3)]
            for j in range(3):
                for i in range(3):
                    new_pl[i][j] = up[j][2-i]
            up = copy.deepcopy(new_pl)

            rot_list = [back, left, front, right]
            temp = []
            
            ij_list = [[(0, 0), (0, 1), (0, 2)], [(0, 0), (0, 1), (0, 2)],
            [(0, 0), (0, 1), (0, 2)],[(0, 0), (0, 1), (0, 2)]]
        
            for i in range(len(rot_list)):
                tmp = []
                for j in range(3):
                    y, x = ij_list[i][j]
                    tmp.append(rot_list[i][y][x])
                temp.append(tmp)
            temp.insert(0, temp.pop(-1))
            
            for i in range(len(rot_list)):
                for j in range(3):
                    y, x = ij_list[i][j]
                    rot_list[i][y][x] = temp[i][j]
        elif cmd == 'D+':
            new_pl = [[0] * 3 for _ in range(3)]
            for j in range(2, -1, -1):
                for i in range(3):
                    new_pl[i][j] = down[2-j][i]
            down = copy.deepcopy(new_pl)

            rot_list = [back, left, front, right]
            temp = []
            
            ij_list = [[(2, 0), (2, 1), (2, 2)], [(2, 0), (2, 1), (2, 2)],
            [(2, 0), (2, 1), (2, 2)],[(2, 0), (2, 1), (2, 2)]]
        
            for i in range(len(rot_list)):
                tmp = []
                for j in range(3):
                    y, x = ij_list[i][j]
                    tmp.append(rot_list[i][y][x])
                temp.append(tmp)
            temp.insert(0, temp.pop(-1))
            
            for i in range(len(rot_list)):
                for j in range(3):
                    y, x = ij_list[i][j]
                    rot_list[i][y][x] = temp[i][j]
        elif cmd == 'D-':
            new_pl = [[0] * 3 for _ in range(3)]
            for j in range(3):
                for i in range(3):
                    new_pl[i][j] = down[j][2-i]
            down = copy.deepcopy(new_pl)

            rot_list = [back, right, front, left]
            temp = []
            
            ij_list = [[(2, 2), (2, 1), (2, 0)], [(2, 2), (2, 1), (2, 0)],
            [(2, 2), (2, 1), (2, 0)],[(2, 2), (2, 1), (2, 0)]]
        
            for i in range(len(rot_list)):
                tmp = []
                for j in range(3):
                    y, x = ij_list[i][j]
                    tmp.append(rot_list[i][y][x])
                temp.append(tmp)
            temp.insert(0, temp.pop(-1))
            
            for i in range(len(rot_list)):
                for j in range(3):
                    y, x = ij_list[i][j]
                    rot_list[i][y][x] = temp[i][j]
        elif cmd == 'F+':
            new_pl = [[0] * 3 for _ in range(3)]
            for j in range(2, -1, -1):
                for i in range(3):
                    new_pl[i][j] = front[2-j][i]
            front = copy.deepcopy(new_pl)

            rot_list = [up, right, down, left]
            temp = []
            
            ij_list = [[(2, 0), (2, 1), (2, 2)], [(0, 0), (1, 0), (2, 0)],
            [(0, 2), (0, 1), (0, 0)],[(2, 2), (1, 2), (0, 2)]]
        
            temp = []
            for i in range(len(rot_list)):
                tmp = []
                for j in range(3):
                    y, x = ij_list[i][j]
                    tmp.append(rot_list[i][y][x])
                temp.append(tmp)
            temp.insert(0, temp.pop(-1))
            
            for i in range(len(rot_list)):
                for j in range(3):
                    y, x = ij_list[i][j]
                    rot_list[i][y][x] = temp[i][j]
        elif cmd == 'F-':
            new_pl = [[0] * 3 for _ in range(3)]
            for j in range(3):
                for i in range(3):
                    new_pl[i][j] = front[j][2-i]
            front = copy.deepcopy(new_pl)

            rot_list = [up, left, down, right]
            temp = []
            
            ij_list = [[(2, 2), (2, 1), (2, 0)], [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (0, 1), (0, 2)], [(2, 0), (1, 0), (0, 0)]]
        
            temp = []
            for i in range(len(rot_list)):
                tmp = []
                for j in range(3):
                    y, x = ij_list[i][j]
                    tmp.append(rot_list[i][y][x])
                temp.append(tmp)
            temp.insert(0, temp.pop(-1))
            
            for i in range(len(rot_list)):
                for j in range(3):
                    y, x = ij_list[i][j]
                    rot_list[i][y][x] = temp[i][j]
        elif cmd == 'B+':
            new_pl = [[0] * 3 for _ in range(3)]
            for j in range(2, -1, -1):
                for i in range(3):
                    new_pl[i][j] = back[2-j][i]
            back = copy.deepcopy(new_pl)

            rot_list = [up, left, down, right]
        
            ij_list = [[(0, 2), (0, 1), (0, 0)], [(0, 0), (1, 0), (2, 0)],
            [(2, 0), (2, 1), (2, 2)], [(2, 2), (1, 2), (0, 2)]]
        
            temp = []
            for i in range(len(rot_list)):
                tmp = []
                for j in range(3):
                    y, x = ij_list[i][j]
                    tmp.append(rot_list[i][y][x])
                temp.append(tmp)
            temp.insert(0, temp.pop(-1))
            
            for i in range(len(rot_list)):
                for j in range(3):
                    y, x = ij_list[i][j]
                    rot_list[i][y][x] = temp[i][j]
        elif cmd == 'B-':
            new_pl = [[0] * 3 for _ in range(3)]
            for j in range(3):
                for i in range(3):
                    new_pl[i][j] = back[j][2-i]
            back = copy.deepcopy(new_pl)

            rot_list = [up, right, down, left]
            temp = []
            ij_list = [[(0, 0), (0, 1), (0, 2)], [(0, 2), (1, 2), (2, 2)],
            [(2, 2), (2, 1), (2, 0)], [(2, 0), (1, 0), (0, 0)]]
        
            temp = []
            for i in range(len(rot_list)):
                tmp = []
                for j in range(3):
                    y, x = ij_list[i][j]
                    tmp.append(rot_list[i][y][x])
                temp.append(tmp)
            temp.insert(0, temp.pop(-1))
            
            for i in range(len(rot_list)):
                for j in range(3):
                    y, x = ij_list[i][j]
                    rot_list[i][y][x] = temp[i][j]
        elif cmd == 'R+':
            new_pl = [[0] * 3 for _ in range(3)]
            for j in range(2, -1, -1):
                for i in range(3):
                    new_pl[i][j] = right[2-j][i]
            right = copy.deepcopy(new_pl)

            rot_list = [up, back, down, front]
            temp = []
            ij_list = [[(2, 2), (1, 2), (0, 2)], [(0, 0), (1, 0), (2, 0)],
            [(2, 2), (1, 2), (0, 2)], [(2, 2), (1, 2), (0, 2)]]
        
            temp = []
            for i in range(len(rot_list)):
                tmp = []
                for j in range(3):
                    y, x = ij_list[i][j]
                    tmp.append(rot_list[i][y][x])
                temp.append(tmp)
            temp.insert(0, temp.pop(-1))
            
            for i in range(len(rot_list)):
                for j in range(3):
                    y, x = ij_list[i][j]
                    rot_list[i][y][x] = temp[i][j]
        elif cmd == 'R-':
            new_pl = [[0] * 3 for _ in range(3)]
            for j in range(3):
                for i in range(3):
                    new_pl[i][j] = right[j][2-i]
            right = copy.deepcopy(new_pl)

            rot_list = [up, front, down, back]
            temp = []
            ij_list = [[(0, 2), (1, 2), (2, 2)], [(0, 2), (1, 2), (2, 2)],
            [(0, 2), (1, 2), (2, 2)], [(2, 0), (1, 0), (0, 0)]]
        
            temp = []
            for i in range(len(rot_list)):
                tmp = []
                for j in range(3):
                    y, x = ij_list[i][j]
                    tmp.append(rot_list[i][y][x])
                temp.append(tmp)
            temp.insert(0, temp.pop(-1))
            
            for i in range(len(rot_list)):
                for j in range(3):
                    y, x = ij_list[i][j]
                    rot_list[i][y][x] = temp[i][j]
        elif cmd == 'L+':
            new_pl = [[0] * 3 for _ in range(3)]
            for j in range(2, -1, -1):
                for i in range(3):
                    new_pl[i][j] = left[2-j][i]
            left = copy.deepcopy(new_pl)

            rot_list = [up, front, down, back]
            temp = []
            ij_list = [[(0, 0), (1, 0), (2, 0)], [(0, 0), (1, 0), (2, 0)],
            [(0, 0), (1, 0), (2, 0)], [(2, 2), (1, 2), (0, 2)]]
        
            temp = []
            for i in range(len(rot_list)):
                tmp = []
                for j in range(3):
                    y, x = ij_list[i][j]
                    tmp.append(rot_list[i][y][x])
                temp.append(tmp)
            temp.insert(0, temp.pop(-1))
            
            for i in range(len(rot_list)):
                for j in range(3):
                    y, x = ij_list[i][j]
                    rot_list[i][y][x] = temp[i][j]
        elif cmd == 'L-':
            new_pl = [[0] * 3 for _ in range(3)]
            for j in range(3):
                for i in range(3):
                    new_pl[i][j] = left[j][2-i]
            left = copy.deepcopy(new_pl)

            rot_list = [up, back, down, front]
            temp = []
            ij_list = [[(2, 0), (1, 0), (0, 0)], [(0, 2), (1, 2), (2, 2)],
            [(2, 0), (1, 0), (0, 0)], [(2, 0), (1, 0), (0, 0)]]
        
            temp = []
            for i in range(len(rot_list)):
                tmp = []
                for j in range(3):
                    y, x = ij_list[i][j]
                    tmp.append(rot_list[i][y][x])
                temp.append(tmp)
            temp.insert(0, temp.pop(-1))
            
            for i in range(len(rot_list)):
                for j in range(3):
                    y, x = ij_list[i][j]
                    rot_list[i][y][x] = temp[i][j]
        #print(up)
        #print(down)
        #print(front)
        #print(back)
        #print(left)
        #print(right)
        #print()  
    ans_list.append(up)
        
def listToString(str_list):
    result = ""
    for s in str_list:
        result += s + ""
    
    return result

for i in range(len(ans_list)):
    for j in range(len(ans_list[i])):
        a = listToString(ans_list[i][j])
        print(a)

     