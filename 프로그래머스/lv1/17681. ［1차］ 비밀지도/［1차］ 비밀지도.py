def solution(n, arr1, arr2):
    answer = []
    secret_map = []
    for i, j in zip(arr1, arr2):
        answer.append(int(bin(i)[2:])+int(bin(j)[2:]))
    for num in answer:
        a = ''
        for i in str(num).zfill(n): #zfill(n)은 왼쪽부터 n자리 수만큼 0으로 채워서 숫자를 반환
            if i == '0':
                a += ' '
            else:
                a += '#'
        secret_map.append(''.join(a))

    return secret_map
    
    #rjust(n, 'x')은 왼쪽부터 n자리 수만큼 'x'로 채워서 반환
