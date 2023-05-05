def solution(s):
    nums = {'0' : 'zero', '1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four', '5' : 'five',
            '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine'}
    for num, eng in nums.items(): #숫자를 정의한 dict for문
        if eng in s: #s에 영단어가 있다면
            s = s.replace(eng, num) #s에서 문자열을 숫자 문자열로 치환하고
    return int(s) #int로 변환 후 return