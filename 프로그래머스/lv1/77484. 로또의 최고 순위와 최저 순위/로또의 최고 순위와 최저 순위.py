def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6} # 맞춘 개수 : 순위 배열
    collect = 0 # 지워지지 않은 개수에서 맞춘 개수
    plus = lottos.count(0) #지워진 번호의 개수

    for lotto in lottos:
        if lotto in win_nums: # 하나의 번호가 정답 로또에 있다면
            collect += 1 # 맞은 개수를 더하기
# 경우의 수
# 전부 알고 있는 경우 collect만 return (plus가 0인 경우)
# 전부 모르는 경우 1, 6을 return (plus가 6인 경우)

    max_score = rank[collect+plus]
    min_score = rank[collect]
    if plus == 6:
        return [1, 6]
    elif plus == 0: # 지워진 번호가 없다면
        return [min_score, min_score]
    elif 0 < plus < 6:
        return [max_score, min_score]