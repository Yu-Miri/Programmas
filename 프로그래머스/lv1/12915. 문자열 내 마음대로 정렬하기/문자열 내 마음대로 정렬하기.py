def solution(strings, n):
    strings.sort() #겹치는 문자열이 있을 경우에 그 다음 문자열을 기준으로 오름차순 정렬하고
    return sorted(strings, key=lambda st : st[n]) #n번째 글자를 기준으로 문자열을 오름차순하여 return