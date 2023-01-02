def solution(topping):
    af = {}
    for i in range(len(topping)):
        try:
            af[topping[i]] += 1
        except:
            af[topping[i]] = 1
    pr = {}
    cnt = 0
    for i in range(len(topping)):
        af[topping[i]] -= 1
        if af[topping[i]] == 0:
            af.pop(topping[i])
        try:
            pr[topping[i]] += 1
        except:
            pr[topping[i]] = 1
        
        if len(pr) == len(af):
            cnt += 1
    return cnt