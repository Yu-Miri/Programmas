def solution(a, b, n):
    answer = 0
    
    while n >= a: # 빈 콜라 병의 개수를 나눌 수 있는 동안
        n, nam = divmod(n, a) # 몫과 나머지를 구하고
        answer += n * b # 교환한 병 수와 교환해 주는 병 수를 곱해서 총 받은 병 수에 더하기
        n = n*b + nam #  보유 병 수와 교환하고 남은 병 수를 더해서 새로 정의
        
    return answer