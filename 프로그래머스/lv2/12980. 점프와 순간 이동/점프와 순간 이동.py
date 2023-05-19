def solution(n):
    ans = 1 # 건전지 사용량, 맨 처음에 한 칸 점프
    while n >= 2:
        if n%2 == 0:
            n = n // 2
        else:
            ans += 1
            n = (n-1) // 2
    return ans