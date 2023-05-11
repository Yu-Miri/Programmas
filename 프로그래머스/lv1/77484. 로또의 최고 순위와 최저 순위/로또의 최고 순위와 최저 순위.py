# def solution(lottos, win_nums):
#     rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6} # 맞춘 개수 : 순위 배열
#     collect = 0 # 지워지지 않은 개수에서 맞춘 개수
#     plus = lottos.count(0) #지워진 번호의 개수

#     for lotto in lottos:
#         if lotto in win_nums: # 하나의 번호가 정답 로또에 있다면
#             collect += 1 # 맞은 개수를 더하기

#     max_score = rank[collect+plus] # 지워진 번호의 개수를 더해서 최고 점수 계산
#     min_score = rank[collect]
#     if plus == 6:
#         return [1, 6]
#     elif plus == 0: # 지워진 번호가 없다면
#         return [min_score, min_score]
#     elif 0 < plus < 6:
#         return [max_score, min_score]
    
#---맞추고 참고---
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt_0 = lottos.count(0) # 지워진 번호의 개수를 저장
    collect = 0

    for num in lottos: # 체크한 번호를 for문
        if num in win_nums: # 정답 번호에 있다면
            collect += 1 # 맞춘 개수에 더하고
    return rank[cnt_0 + collect], rank[collect] # 맞춘 개수에 지워진 개수와 맞춘 개수를 return
