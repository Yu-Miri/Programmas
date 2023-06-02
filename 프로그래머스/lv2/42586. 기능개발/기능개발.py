def solution(progresses, speeds):
    answer = []
    distribution = []
    for pro, spd in zip(progresses, speeds):
        day, plus = (divmod((100-pro),spd))
        if plus!=0:
            day+=1
        distribution.append(day)

    add_pro = 1
    first = distribution[0]
    for i in range(1, len(distribution)):
        second = distribution[i]
        if first >= second: 
            add_pro += 1
        else:
            answer.append(add_pro)
            add_pro = 1
            first = distribution[i]
    answer.append(add_pro)

    return answer