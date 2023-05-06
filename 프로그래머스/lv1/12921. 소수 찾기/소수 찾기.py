def solution(n):
    # answer = 1 # 소수인 2를 더하고 시작
    # for n in range(3, n+1): # 소수인지 판별하기 위해 3부터 n까지 for문
    #     for i in range(2, n): # 2부터 n-1까지 for문 돌면서
    #         if n % i == 0: # n이 i로 한 번이라도 나누어 떨어지면 소수가 아니므로 break
    #             break
    #     else:
    #         answer+=1 # 소수라면 answer에 계속 더해서 반환
    # return answer
    
    #에라토스테네스의 체
    num = set(range(2, n+1)) # 2부터 n까지의 범위를 set으로 선언
    
    for i in range(2, n+1): # 2부터 n까지 for문 돌면서
        num -= set(range(2*i, n+1, i)) # 2에 i를 곱한 수부터 num에서 제거
    return len(num)    