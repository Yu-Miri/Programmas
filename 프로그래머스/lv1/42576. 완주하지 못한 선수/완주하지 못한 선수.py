def solution(participant, completion):
    # return ''.join(list(set(participant)-set(completion)))
    participant.sort()
    completion.sort()
    # 오름차순 정렬 후
    
    for i, j in zip(participant, completion):
        if i != j: # 다른 이름이 나오는 경우
            return i # 완주 명단에 없는 i를 return
    return participant[-1] # 끝까지 같다면 마지막 사람이 중복된 이름의 미완주자