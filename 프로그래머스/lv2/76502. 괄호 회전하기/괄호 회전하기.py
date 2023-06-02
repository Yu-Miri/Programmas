def solution(s):
    answer = 0
    chk_list = [s]
    for i in range(len(s)-1):
        s = s[1:]+s[0]
        chk_list.append(s)
    
    for str in chk_list:
        stack = []
        for i in str:
            if len(stack) == 0:
                stack.append(i)
            else:
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(i)
        if len(stack) == 0:
            answer += 1
        
    return answer
