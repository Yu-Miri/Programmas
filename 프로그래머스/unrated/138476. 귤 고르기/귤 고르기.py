from collections import Counter
def solution(k, tangerine):
    cnt = 0
    k = k
    tan = sorted(Counter(tangerine).items(), key= lambda x:x[1],reverse=True)
    for scale, num in tan:
        k -= num
        cnt += 1
        if k <= 0:
            return cnt