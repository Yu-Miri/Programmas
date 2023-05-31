def solution(elements):
    answer = set()
    ele_len = len(elements)
    elements = elements * 2 

    for i in range(ele_len): # 길이만큼만 돌아서 계산할 범위
        for j in range(ele_len): # 현재 idx부터 합 계산
            answer.add(sum(elements[j:j+i+1]))
    return len(answer)