def solution(want, number, discount):
    answer = 0
    want_dict = {}
    for i, item in enumerate(want):
        want_dict[item] = number[i]
    
    for i in range(len(discount)-9):
        temp = {}
        for j in range(10):
            try:
                temp[discount[i+j]] += 1
            except:
                temp[discount[i+j]] = 1
        det = 0
        
        for key, val in want_dict.items():
            try:
                if temp[key] < want_dict[key]:
                    det = 1
                    break
            except:
                det = 1
                break
        if det == 0:
            answer +=1 
            
    
    return answer