def solution(number, limit, power):
    # yak = 1
    # for i in range(2, number+1):
    #     num = 0
    #     for j in range(1, i+1):
    #         if i % j == 0: # 약수라면
    #             num += 1 # num에 더해서 

    #     if num <= limit: # 약수의 개수가 제한 수보다 작다면
    #         yak += num # num을 더하고
    #     else:
    #         yak += power # 크다면 power을 더하기
    # return yak

    yak = 1
    for i in range(2, number+1):
        num = 0
        for j in range(1, int(i**0.5)+1): # 최대 기사단원의 수에 제곱근을 통해 절반으로 범위를 줄이기
            if i % j == 0: # 약수라면
                num += 1 # 1을 더해주고
                if j ** 2 != i: # 제곱이 되는 약수가 중복일 수 있으므로
                    num += 1 # 한 번 더 더하기

        if num <= limit: # limit보다 num이 작은 경우에
            yak += num # num을 더하고
        else: #큰 경우에
            yak += power # power을 더하기 
    return yak
print(solution(10, 3, 2))