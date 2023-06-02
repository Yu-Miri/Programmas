def solution(s):
    answer = 0
    chk_list = [s]
    for i in range(len(s)-1): # 회전한 괄호 리스트
        s = s[1:]+s[0]
        chk_list.append(s)
    
    for str in chk_list:
        stack = []
        for i in str:
            if len(stack) == 0:
                stack.append(i)
            else: # 비교해야 할 괄호가 있다면 하나씩 비교해서 제대로 닫힌 괄호라면 제거
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                else: #그렇지 않다면 추가
                    stack.append(i)
        if len(stack) == 0: # 올바른 괄호라면 1 더해주기
            answer += 1
        
    return answer
