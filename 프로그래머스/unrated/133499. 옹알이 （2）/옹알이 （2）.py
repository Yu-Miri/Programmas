# def solution(babbling):
#     # answer = 0
#     # ongal = ["aya", "ye", "woo", "ma"]
#     # for bab in babbling:
#     #     for ong in ongal:
#     #         if ong in bab:
#     #             bab = bab.replace(ong, '', 1)
#     #             # 연속된 발음은 할 수 없으므로 하나만 제거
#     #     if len(bab)==0:
#     #         answer += 1
#     # return answer

#     answer = 0
#     ongal = ["aya", "ye", "woo", "ma"]
#     for bab in babbling:
#         for ong in ongal:
#             bab = bab.replace(ong, ' ', 1)
#                 # 연속된 발음은 할 수 없고,
#                 # 가운데 발음 제거 후 남은 발음 중복 제거 방지
#         if bab.isspace():
#             answer += 1
#     return answer
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
                print("i =", i)
        if len(i.strip())==0:
            answer +=1
    return answer