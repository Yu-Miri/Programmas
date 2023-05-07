def solution(N, stages):
#     f_ratio = [] # 실패율
#     fail_stage = [] # f_ratio에서 실패율 높은 순서의 index
#     ls = len(stages) # 스테이지에 도달한 플레이어 수

#     for i in range(1,N+1): # 스테이지 수 만큼 for문
#         f_ratio.append(stages.count(i)/ls) # 각 스테이지마다 실패율을 계산해서 더하기
#         ls -= stages.count(i) # 다음 스테이지에 대해서 현재 스테이지에 머물러 있는 플레이어 수 빼기

#     new_an = sorted(list(set(f_ratio)), reverse=True) # 중복 값을 제거한 후에 정렬


#     for j in new_an: #중복 제거한 실패율 리스트 for문
#         fail_stage.extend(list(filter(lambda x:f_ratio[x] == j, range(len(f_ratio)))))
#         # 플레이어 수만큼 돌면서 중복 제거 전의 실패율 리스트(f_ratio)에서 실패율(i)이 중복으로 존재하는 값을 전부 찾아서 리스트에 index를 더하기
#     return [rank + 1 for rank in fail_stage]

    fail_stage = {}
    ls = len(stages) # 스테이지에 도달한 플레이어 수

    for i in range(1,N+1): # 스테이지 번호 for문
        if ls != 0:
            fail_stage[i] = stages.count(i)/ls  # 각각의 스테이지와 실패율을 계산해서 딕셔너리에 추가
            ls -= stages.count(i) # 다음 스테이지에 대해서 실패한 플레이어 수 빼기
        else:
            fail_stage[i] = 0
    return sorted(fail_stage, key=lambda i: fail_stage[i], reverse=True)
    #fail_stage의 value값을 기준으로 내림차순 정렬해서 key값을 return