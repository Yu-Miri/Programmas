def solution(s):
    cnt = 0
    zero_cnt = s.count('0')
    while int(s) >= 10:
        s = bin(s.count('1'))[2:]
        cnt += 1
        zero_cnt += s.count('0')

    return [cnt, zero_cnt]