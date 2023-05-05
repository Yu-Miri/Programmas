def solution(t, p):
    answer = 0
    le = len(p) #p의 길이를 저장하고
    
    for i in range(len(t)): #t의 길이만큼 for문 돌면서
        a = t[i:i+le] #index 위치부터 p의 길이만큼을 저장하고
        if len(a) == le and int(a) <= int(p): #a의 길이가 p의 길이와 같고 p가 더 크다면
            answer += 1 #1을 더해가면서 return
    
    return answer