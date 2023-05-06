def solution(answers):
    #각 수포자가 찍는 패턴을 리스트에 선언
    std1 = [1,2,3,4,5]
    std2 = [2,1,2,3,2,4,2,5]
    std3 = [3,3,1,1,2,2,4,4,5,5]

    correct_num = [0, 0, 0]
    for idx, ans in enumerate(answers): #정답지 패턴의 길이만큼 for문
        if std1[idx%len(std1)] == ans: # i를 수포자의 패턴 길이로 나눠서 인덱스를 반복
            correct_num[0] += 1 # 정답과 같다면 해당 인덱스에 1을 더하기
        if std2[idx%len(std2)] == ans:
            correct_num[1] += 1
        if std3[idx%len(std3)] == ans:
            correct_num[2] += 1

    best = max(correct_num)
    return [idx+1 for idx, num in enumerate(correct_num) if num == best]
    # 정답 개수의 인덱스와 값을 for문돌면서 값과 가장 높은 값이 같다면 idx에 1을 더해서 return
