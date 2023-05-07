def solution(k, m, score):
    # answer = 0
    # score.sort(reverse=True) # 내림차순 정렬 후
    # for i in range(len(score)//m): # 사과의 총 개수에서 한 상자에 담아야 하는 사과의 개수를 나눈 몫만큼 for문
    #     answer += min(score[:m]) * m # 가장 작은 값에 사과 개수를 곱해서 더하고
    #     del score[:m] #담은 사과는 제거
    # return answer
    
    return sum(sorted(score)[len(score)%m::m])*m
    # 정렬 후 총 사과 개수에서 한 상자에 담아야 하는 사과 개수 m을 나눈 나머지부터 m씩 건너 뛰면서 리스트에 저장하고
    # 리스트에 저장된 최저 사과 점수를 전부 더하고 한 상자에 담긴 사과 개수를 곱해서 return 