def solution(k, tangerine):
    t_dict = {}
    for i in range(len(tangerine)):
        try:
            t_dict[tangerine[i]] += 1
        except:
            t_dict[tangerine[i]] = 1
    t_tup= sorted(t_dict.items(), key=lambda x:-x[1])
    
    counter = 0
    answer = 0
    for i in range(len(t_tup)):
        key, val = t_tup[i]
        counter += val
        if counter < k:
            answer += 1
        else:
            answer += 1
            break
            
    return answer