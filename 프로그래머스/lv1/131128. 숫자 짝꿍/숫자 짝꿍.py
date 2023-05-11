def solution(X, Y):
    answer = ''
    for i in range(10): # 10번의 for문
        min_cnt = min(X.count(str(i)), Y.count(str(i))) # 0의 개수를 각각 구해서 둘 중 작은 값을 저장하고
        answer += str(i) * min_cnt # i를 겹치는 개수 만큼 곱하기
    if len(list(set(answer))) == 1 and list(set(answer))[0] == '0': # 겹치는 개수가 0만 존재한다면
        return '0' # 0을 반환
    elif len(answer) == 0: # 겹치지 않는다면
        return '-1' # -1을 반환
    else: # 두 경우 해당되지 않는다면
        return ''.join(sorted(answer, reverse=True)) # 내림차순 정렬 후 문자열 합치기
