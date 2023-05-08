def solution(cards1, cards2, goal):
    # answer = []
    # for i in goal: # 목표 문장 for문
    #     try:
    #         if i == cards1[0]: # 카드뭉치 1 첫 번째 카드가 i와 같다면 
    #             cards1.pop(0) # 맨 앞에 카드 제거
    #         elif i == cards2[0]: # 카드뭉치 2 첫 번째 카드가 i와 같다면
    #             cards2.pop(0) # 맨 앞에 카드 제거
    #     except: # cards1의 카드뭉치가 전부 제거되어 에러가 뜬다면
    #         if i == cards2[0]: # 카드뭉치 2 첫 번재 카드와 비교해서 i와 같다면
    #             cards2.pop(0) # 맨 앞에 카드 제거
    #         else: # 같지 않다면
    #             return "No" # No return
    # return "Yes" # 전부 통과하면 Yes return
    # answer = []
    for i in goal: # 목표 문장 for문
        if len(cards1) and i == cards1[0]:
            cards1.pop(0)
        elif len(cards2) and i == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"