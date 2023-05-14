def solution(s):
    cnt = 0
    same = 0
    diff = 0
    for i in s:
        if same == diff: # 같은 경우에
            cnt += 1 # 새로 시작하는 문자 체크
            first = i # 비교할 문자로 선언
        if first == i: 
            same += 1 # 다음과 비교하기 위해 same에 1을 더한 상태로 시작
        else:
            diff += 1
    return cnt
