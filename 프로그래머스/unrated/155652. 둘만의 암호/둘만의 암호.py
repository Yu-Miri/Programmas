# def solution(s, skip, index):
#     answer = ''
#     alp = 'abcdefghijklnmopqrstuvwxyz'
#     for sk in skip:
#         if sk in alp:
#             alp = alp.replace(sk, '')

#     for ss in s:
#         target = alp[(alp.index(ss) + index) % len(alp)]
#         # 문자열의 길이가 초과되는 경우에 나머지를 활용하자.
#         answer += target
#     return answer
def solution(s, skip, index):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    for i in list(skip):
        alpha = alpha.replace(i,"")
        
    for a in s:
        answer += alpha[(alpha.find(a) + index) % len(alpha)]
    return answer