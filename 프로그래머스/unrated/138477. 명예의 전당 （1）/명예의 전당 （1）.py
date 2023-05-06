def solution(k, score):
#     worst_rank = []
#     ranking = [0 for i in range(k)] # 명예의 전당 자리만큼 리스트 생성

#     for s in score:
#         if s >= ranking[ranking.index(min(ranking))]: # s가 ranking에서 가장 작은 값보다 크다면
#             ranking[ranking.index(min(ranking))] = s # ranking에서 가장 작은 값의 index 자리를 s로 대체
#         worst_rank.append(min(ranking)) # 최하위 점수를 worst_rank 추가

#     for i in range(k-1): # 처음에 생성된 명예의 전당 자리에 존재하는 0 값을
#         worst_rank[i] = min(score[:i+1]) # score[:i+1]의 가장 작은 값으로 대체
        
#     return worst_rank
    worst_rank = []
    ranking = []
    for s in score: # score for문 돌면서
        ranking.append(s) # ranking에 추가
        ranking = sorted(ranking, reverse=True)[:k] 
        # 내림차순 정렬 후 명예의 전당 자리 수만큼 끊어서

        worst_rank.append(min(ranking)) # 명예의 전당에서 최하위 점수를 추가

    return worst_rank
