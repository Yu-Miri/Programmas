# def solution(n, lost, reserve):
#     re_res = set(reserve) - set(lost) # lost와 중복되는 번호 삭제
#     re_lost = set(lost) - set(reserve) # reserve와 중복되는 번호 삭제
    
#     for i in re_res: 
#         if i + 1 in re_lost:
#             re_lost.remove(i+1)
#         elif i - 1 in re_lost:
#             re_lost.remove(i-1)

#     return n - len(re_lost)
def solution(n, lost, reserve):
    reserve_student = set(reserve) - set(lost)
    
    lost_student = set(lost) - set(reserve)
    
    for student in reserve_student:
        if (student - 1) in lost_student:
            lost_student.remove(student - 1)
        elif (student + 1) in lost_student:
            lost_student.remove(student + 1)
            
    return n - len(lost_student)