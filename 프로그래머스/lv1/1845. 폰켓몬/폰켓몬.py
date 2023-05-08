def solution(nums):
    return min(len(set(nums)), len(nums)/2)
# 가지고 갈 수 있는 nums/2 개수와 unique한 nums의 폰켓몬 개수 중 min 값을 return
