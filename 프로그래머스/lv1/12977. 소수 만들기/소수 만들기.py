import itertools

def solution(nums):
    answer = 0
    for i in itertools.combinations(nums, 3): # 숫자 배열에서 3개의 모든 조합을 for문
        for j in range(2, sum(i)): # 2부터 조합의 합을 for문
            if sum(i) % j == 0: #나누어 떨어지면 소수가 아니므로 break
                break
        else: # for문이 break로 끊기지 않고 끝까지 수행된다면
            answer += 1 #소수라면 answer에 1을 더해 소수의 개수를 return

    return answer