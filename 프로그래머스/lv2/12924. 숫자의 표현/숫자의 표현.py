def solution(n):
    cnt = 1 # 마지막에 자기 자신 하나만 더할 경우도 해당
    #for문은 절반까지만 돌기 때문에 1을 더하고 시작
    for i in range(1, n//2+2):
        sum = 0
        for j in range(i, n):
            sum += j
            if sum==n:
                cnt += 1
                break
            elif sum>n:
                break
    return cnt