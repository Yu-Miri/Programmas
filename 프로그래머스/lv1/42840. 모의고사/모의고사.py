# def solution(answers):
#     su1 = [1, 2, 3, 4, 5]
#     su2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     su3 = [3, 3, 1, 1, 2, 2, 4, 5]
#     num_list = [0, 0, 0]

#     # for i in range(len(answers)):
#     #     if su1[i] == answers[i]:
#     #         num_list[0] += 1
#     #     if su2[i] == answers[i]:
#     #         num_list[1] += 1
#     #     if su3[i] == answers[i]:
#     #         num_list[2] += 1
#     for i in range(len(answers)):
#         if su1[i%5] == answers[i]:
#             num_list[0] += 1
#         if su2[i%8] == answers[i]:
#             num_list[1] += 1
#         if su3[i%10] == answers[i]:
#             num_list[2] += 1

#     best_nums = []
#     for idx, num in enumerate(num_list):
#         if num == max(num_list):
#             best_nums.append(idx+1)

#     return best_nums

def solution(answers):
    
    answer = []
    score = [0,0,0]
    
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)) :
        if answers[i] == student1[i%5] :
            score[0] += 1
        if answers[i] == student2[i%8] :
            score[1] += 1
        if answers[i] == student3[i%10] :
            score[2] += 1
        
    for idx, num in enumerate(score) :
        if num == max(score) :
            answer.append(idx +1)
    
    return answer