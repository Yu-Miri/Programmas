def solution(food):
    answer = ''
    for i in range(len(food)): #음식의 개수만큼 for문
        answer += str(i)*(food[i]//2) #i번째 있는 음식의 개수를 2로 나눈 몫을 음식의 index를 곱해서 문자열로 더한 후에
    answer += '0' + answer[::-1] #0번 칼로리를 더하고, 거꾸로 된 answer를 다시 더해서 return
    
    return answer