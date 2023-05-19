def solution(n,a,b):
    answer = 0

    while max(a,b)-min(a,b) > 0:
        a, b = (a+1)//2, (b+1)//2
        answer += 1

    return answer