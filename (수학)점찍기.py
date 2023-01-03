def solution(k, d):
    x = []
    for i in range(10**9):
        if i * k > d:
            break
        x.append(i*k)
    answer =0
    for i in x:
        y = int((d**2 - i**2)**0.5)
        answer += y//k+1
    return answer