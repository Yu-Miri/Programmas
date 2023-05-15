def solution(s):
    s = s.split(' ')
    s = list(map(lambda x : x.capitalize(), s))

    return ' '.join(s)