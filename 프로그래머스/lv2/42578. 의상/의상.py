from collections import Counter
def solution(clothes):
    fashion = []
    for i in clothes: # 종류를 하나씩 담아서 저장
        fashion.append(i[1])

    fashion_num = Counter(fashion) # 하나의 종류에 대해서 경우의 수 세기

    for j in fashion_num: # 입지 않은 경우도 있으므로 1을 더해주기
        fashion_num[j] += 1

    values = 1
    for _, value in fashion_num.items():
        values *= value

    return values - 1 # 한 의상은 무조건 입어야 하기 때문에 아예 입지 않은 경우는 삭제