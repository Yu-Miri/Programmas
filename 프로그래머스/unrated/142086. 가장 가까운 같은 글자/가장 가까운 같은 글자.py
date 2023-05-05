def solution(s):
    answer = []
    for idx, i in enumerate(s): #index와 문자열을 차례로 반환하여
        if i not in s[:idx]: #index 전까지 i가 없다면 
            answer.append(-1) #-1 추가
        else: #있으면
            answer.append(idx - s[:idx].rfind(i)) #오른쪽에서부터 몇 번째에 있는지 찾고 해당 index를 빼서 차이나는 칸 수를 더한다
    return answer