def solution(s, skip, index):
    answer = ""
    alp = "abcdefghijklmnopqrstuvwxyz"
    for sk in list(skip):
        alp = alp.replace(sk, "")

    for ss in s:
        answer += alp[(alp.find(ss) + index) % len(alp)]
        # 문자열의 길이가 초과되는 경우에 나머지를 활용하자.
    return answer

# def solution(s, skip, index):
#     alpha = "abcdefghijklmnopqrstuvwxyz"
#     answer = ""
#     for i in list(skip):
#         alpha = alpha.replace(i,"")
        
#     for a in s:
#         answer += alpha[(alpha.find(a) + index) % len(alpha)]
#     return answer