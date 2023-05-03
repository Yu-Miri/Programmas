import numpy as np

def solution(arr1, arr2):
    a = np.array(arr1)
    b = np.array(arr2)
    res = a+b # numpy 행렬 덧셈
    return res.tolist() # 리스트로 변환