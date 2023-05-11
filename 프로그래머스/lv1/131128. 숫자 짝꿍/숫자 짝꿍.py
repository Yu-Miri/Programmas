def solution(X, Y):
    answer = ''
    zero_chk = 0
    number = []
    for i in range(10): #0,9까지 for문 돌면서 0의 개수를 각각 구해서 replace(더 작은 쪽의 개수만큼 치환하고) 개수만큼 answer에 더해준다
        min_cnt = min(X.count(str(i)), Y.count(str(i))) # 0의 개수를 각각 구해서 둘 중 작은 값을 저장하고
        answer += str(i) * min_cnt # i를 겹치는 개수 만큼 곱하기
    if len(list(set(answer))) == 1 and list(set(answer))[0] == '0': # 겹치는 개수가 0만 존재한다면
        return '0'
    elif len(answer) == 0: # 겹치지 않는다면
        return '-1' # -1을 반환
    else: # 두 경우 해당되지 않는다면
        return ''.join(sorted(answer, reverse=True)) # 내림차순 정렬 후 문자열 합치기