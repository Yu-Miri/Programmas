def solution(n, arr1, arr2):
    answer = []
    secret_map = []
    for i, j in zip(arr1, arr2):
        answer.append(int(bin(i)[2:])+int(bin(j)[2:]))
    for num in answer:
        a = ''
        for i in str(num).zfill(n):
            if i == '0':
                a += ' '
            else:
                a += '#'
        secret_map.append(''.join(a))

    return secret_map