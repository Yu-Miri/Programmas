def solution(babbling):
    # answer = 0
    # ongal = ["aya", "ye", "woo", "ma"]
    # for bab in babbling:
    #     for ong in ongal:
    #         bab = bab.replace(ong, '.', 1)
    #             # 연속된 발음은 할 수 없고,
    #             # 가운데 발음 제거 후 남은 발음 중복 제거 방지
    #     if bab.replace('.','') == '':
    #         answer += 1
    # return answer
    
    answer = 0
    ongal = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        for ong in ongal:
            if ong*2 not in bab: # 연속된 발음이 아닌 경우
                bab = bab.replace(ong, '.')
                # 가운데 발음 제거 후 남은 발음 중복 제거 방지
                # 떨어져 있는 발음은 가능하기 때문에 하나만 제거하면 테스트 오류
        if bab.replace('.','') == '':
            answer += 1
    return answer
