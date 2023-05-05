def solution(array, commands):
    answer = []
    for i, j, k in commands: # 2차원 배열들을 for문 돌면서
        answer.append(sorted(array[i-1:j])[k-1]) #배열의 i번째부터 j까지 자르고 정렬해서 k번째에 있는 수를 구해서 추가
    return answer
