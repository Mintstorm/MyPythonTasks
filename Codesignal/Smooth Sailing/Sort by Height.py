import numpy as np
def solution(a):
    a
    a=np.array(a)
    a[a>0]=np.sort(a[a>0])
    return a
