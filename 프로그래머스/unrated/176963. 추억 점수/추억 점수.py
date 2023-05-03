def solution(name, yearning, photo):
    answer = []
    for i in photo: #계산해야 하는 photo 개수 만큼 for문
        yearn = 0 
        for j in i: #한 장에 있는 사람 한 명에 대해
            try:
                yearn += yearning[name.index(j)] # 그리움 점수를 더하고
            except:
                pass # 그리움을 담은 리스트에 없으면 pass
        answer.append(yearn)
    return answer
