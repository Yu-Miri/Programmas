def solution(d, budget):
    d.sort()
    while budget < sum(d): # budget이 모든 부서의 지원 금액보다 작은 경우
        d.pop() # 맨 마지막 index(가장 큰 값)를 제거
    return len(d) # budget이 부서들의 지원 금액과 같거나 큰 경우에 남은 부서의 개수 return