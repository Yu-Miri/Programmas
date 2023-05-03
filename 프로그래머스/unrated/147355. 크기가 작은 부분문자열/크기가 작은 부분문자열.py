def solution(t, p):
    answer = []
    le = len(p)
    
    for i in range(len(t)):
        a = t[i:i+le]
        if len(a) == le and int(a) <= int(p):
            answer.append(a)
    
    return len(answer)