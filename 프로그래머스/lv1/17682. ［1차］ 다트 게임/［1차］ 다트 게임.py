def solution(dart):
    # answer = ''
    # nums = re.findall('[0-9]', dart)
    # strs = {'S': '1', 'D' : '2', 'T' : '3', "#" : '*(-1)', '*' : '*2'}
    # star_chk = 0
    # for i in re.findall('[^0-9]', dart): # 숫자를 제외한 S, D, T, *, # 을 찾아서 for문
    #     if i in ['S', 'D', 'T'] and dart[dart.index(i)+1]=='*' and star_chk > 0:
    #         answer = answer[:-1] + '*2+'+ dart[dart.index(i) - 1] + '**' + strs[i] + '*2+'
    #     elif i in ['S', 'D', 'T'] and star_chk == 0:
    #         answer += dart[dart.index(i) - 1] + '**' + strs[i] + '+'
    #     elif i == '#':
    #         answer = answer[:-1] + '*(-1)' + '+' # 더해져 있는 수식의 끝에 더하기 연산자 삭제 후 추가해주기
    #     elif i == '*' and star_chk == 0:
    #         answer = answer[:-1] +'*2+'
    # return eval(answer[2:-1])

    n = ''
    score = []
    for i in dart: # 완전 탐색
        if i.isnumeric(): # 숫자라면
            n += i # 1의 자리가 아닌 경우에도 숫자를 제대로 곱할 수 있음
        elif i == 'S':
            score.append(int(n)**1)
            n = ''
        elif i == 'D':
            score.append(int(n)**2)
            n = ''
        elif i == 'T':    
            score.append(int(n)**3)
            n = ''
        elif i =='#':
            score[-1] = score[-1] * (-1)
        elif i =='*':
            if len(score) > 1: # 처음 나온 스타상이 아니라면
                score[-2] = score[-2] * 2 # 이전의 점수에 2배
                score[-1] = score[-1] * 2 # 받은 점수에 2배
            else:
                score[-1] = score[-1] * 2 # 처음 나온 스타상이라면 받은 점수에 2배
    return sum(score)